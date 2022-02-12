
from django.urls import path

from api.views import BlogListAPIView, BlogListRetrieveAPIView, blogCreate, blogUpdate, blogDelete

app_name = 'api'

urlpatterns = [
    path('blog/', BlogListAPIView.as_view()),
    path('blog-create/', blogCreate, name='create-blog'),
    path('blog-update/<int:pk>/', blogUpdate, name='update-blog'),
    path('blog-delete/<int:pk>/', blogDelete, name='delete-blog'),
    path('blog/<int:pk>/', BlogListRetrieveAPIView.as_view()),
]






