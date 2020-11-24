from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def dispatch(self, request, *args, **kwargs):
        print("request.body: ",request.body) # print 비추천, logger 추천!
        print("request.POST: ",request.POST)
        return super().dispatch(request, *args, **kwargs)