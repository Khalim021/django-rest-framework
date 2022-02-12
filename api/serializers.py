from rest_framework import serializers

from blog.models import CategoryModel, TagModel, BlogListModel


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class TagModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = '__all__'


class BlogListModelSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    tags = TagModelSerializer(many=True)

    class Meta:
        model = BlogListModel
        exclude = ['bio', 'quotes', 'description']
