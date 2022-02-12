from django.urls import path

from blog.views import BlogListView, BlogDetailView, LikeView, ProfileCreateView, updateProfile, deleteProfile

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('profile/', ProfileCreateView.as_view(), name='create-profile'),
    path('likes', LikeView, name='blog-likes'),
    path('update/<int:pk>/', updateProfile, name='update-profile'),
    path('delete/<int:pk>/', deleteProfile, name='delete-profile'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
]





