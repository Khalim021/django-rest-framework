from django.contrib import admin

from blog.models import BlogListModel, CategoryModel, TagModel, LikeModel


@admin.register(BlogListModel)
class BlogListModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'bio', 'quotes', 'description', 'post_views']
    list_filter = ['created_at', 'updated']
    search_fields = ['name', 'quotes', 'description']


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created']


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['created']


@admin.register(LikeModel)
class LikeModelAdmin(admin.ModelAdmin):
    list_display = ['blog']
