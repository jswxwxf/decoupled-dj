from rest_framework.generics import ListAPIView, RetrieveAPIView
from ..models import Blog
from .serializers import BlogSerializer


class BlogList(ListAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()


class BlogDetail(RetrieveAPIView):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
