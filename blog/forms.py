from django import forms

from blog.models import BlogListModel


class ProfileModelForm(forms.ModelForm):
    class Meta:
        model = BlogListModel
        exclude = ['created_at', 'updated', 'likes', 'post_views']






