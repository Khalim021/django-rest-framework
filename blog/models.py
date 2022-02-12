from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class TagModel(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'


class BlogListModel(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField(max_length=150)
    quotes = models.TextField(max_length=310)
    image = models.ImageField(upload_to='blog-images')
    category = models.ForeignKey(CategoryModel, related_name='blog_category',
                                 on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagModel, related_name='blog_tags')
    likes = models.ManyToManyField(User, related_name='likes')
    post_views = models.IntegerField(default=0, null=True, blank=True)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def total_likes(self):
        return self.likes.all().count()

    class Meta:
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'


LIKE_CHOICES = (
    ('Likes', 'Likes'),
    ('Unlike', 'Unlike')
)


class LikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(BlogListModel, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=15)

    def __str__(self):
        return str(self.blog)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
