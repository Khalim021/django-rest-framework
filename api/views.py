# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from api.serializers import BlogListModelSerializer
from blog.models import BlogListModel


class BlogListAPIView(ListAPIView):
    serializer_class = BlogListModelSerializer
    queryset = BlogListModel.objects.order_by('-pk')


class BlogListRetrieveAPIView(RetrieveAPIView):
    serializer_class = BlogListModelSerializer
    queryset = BlogListModel.objects.all()


@api_view(['POST'])
def blogCreate(request):
    serializer = BlogListModelSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def blogUpdate(request, pk):
    blog = BlogListModel.objects.get(id=pk)
    serializer = BlogListModelSerializer(instance=blog, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def blogDelete(request, pk):
    blog = BlogListModel.objects.get(id=pk)

    blog.delete()

    return Response('Blog is successfully deleted')






