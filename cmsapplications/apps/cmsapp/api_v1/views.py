from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
from apps.cmsapp.models import (
    Post,
    Like,
)
from apps.cmsapp.api_v1.serializers import (
    PostSerializer,
    LikeSerializers,
)
from django.db.models import Q

 

class PostAPIViewSet(ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

    def create(self, request, *args, **kwargs):

        user_id = request.data.get('user')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=user_id)
        return Response(
            data={
                "error": False,
                "data": [serializer.data],
                "message": "Create Post Successfully.",
            },
            status=status.HTTP_201_CREATED,
        )

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user

        if user.is_authenticated:
            queryset = queryset.filter(Q(user=user) | Q(user__isnull=True))
        return queryset


    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            raise PermissionDenied("You do not have permission to update this post.")

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            raise PermissionDenied("You do not have permission to delete this post.")

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikeViewSet(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializers

    def create(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        user_id = request.data.get('user')

        like, created = Like.objects.get_or_create(post_id=post_id, user_id=user_id)

        if not created:
            return Response({'detail': 'Already liked.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Post liked successfully.'}, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['post'])
    def unlike(self, request, *args, **kwargs):
        post_id = request.data.get('post')
        user_id = request.data.get('user')

        like = get_object_or_404(Like, post_id=post_id, user_id=user_id)
        like.delete()

        return Response({'detail': 'Post unliked successfully.'}, status=status.HTTP_200_OK)
