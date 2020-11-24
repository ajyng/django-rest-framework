from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .serializers import PostSerializer
from .models import Post

class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body: ",request.body) # print 비추천, logger 추천!
        print("request.POST: ",request.POST)
        return super().dispatch(request, *args, **kwargs)