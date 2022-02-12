from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import ProfileModelForm
from blog.models import BlogListModel, LikeModel


def LikeView(request):
    user = request.user
    if request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        blog = BlogListModel.objects.get(id=blog_id)

        if user in blog.likes.all():
            blog.likes.remove(user)
        else:
            blog.likes.add(user)
        likes, created = LikeModel.objects.get_or_create(user=user, blog_id=blog_id)

        if not created:
            if likes.value == 'Like':
                likes.value = 'Unlike'
            else:
                likes.value = 'Like'
        likes.save()

    return redirect('/')


class BlogListView(ListView):
    template_name = 'blog-list.html'

    def get_queryset(self):
        qs = BlogListModel.objects.order_by('-pk')

        return qs


class BlogDetailView(DetailView):
    template_name = 'blog-detail.html'
    model = BlogListModel

    def get_object(self, queryset=None):
        object = super().get_object()
        object.post_views = object.post_views + 1
        object.save()
        return object


class ProfileCreateView(CreateView):
    template_name = 'form-list.html'
    form_class = ProfileModelForm

    def get_success_url(self):
        return reverse('blog:blog-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Create Profile'
        return context


def updateProfile(request, pk):
    blog = BlogListModel.objects.get(id=pk)
    form = ProfileModelForm(instance=blog)

    if request.method == 'POST':
        form = ProfileModelForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'form-list.html', context)


def deleteProfile(request, pk):
    blog = BlogListModel.objects.get(id=pk)
    if request.method == "POST":
        blog.delete()
        return redirect('/')

    context = {
        'item': blog
    }
    return render(request, 'delete.html', context)
