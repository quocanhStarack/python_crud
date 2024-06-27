from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from post.models import Post
from post.serializers import PostSerializer
from rest_framework import status


# Create your views here.

class PostView(ListCreateAPIView):
    model = Post
    serializer_class = PostSerializer

    def get_queryset(self):
        print(self.request.query_params)
        return Post.objects.all()
    
    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Create a new Post successful!'
            }, status= status.HTTP_201_CREATED)

        return JsonResponse({
            'message': 'Create a new Post unsuccessful!'
        }, status= status.HTTP_400_BAD_REQUEST)
    
class UpdateDeletePostView(RetrieveUpdateDestroyAPIView):
    model = Post
    serializer_class = PostSerializer

    def put(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get('pk'))
        serializer = PostSerializer(post, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return JsonResponse({
                'message': 'Update Post successful!'
            }, status=status.HTTP_200_OK)

        return JsonResponse({
            'message': 'Update Post unsuccessful!'
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        post = get_object_or_404(Post, id=kwargs.get('pk'))
        post.delete()

        return JsonResponse({
            'message': 'Delete post successful!'
        }, status=status.HTTP_200_OK)
