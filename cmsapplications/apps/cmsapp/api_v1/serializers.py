from rest_framework import serializers
from apps.cmsapp.models import (
    Post,
    Like,
)
from django.db.models import Sum


class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    liked_by = LikeSerializers(many=True, read_only=True, source='blog_post')
    liked_count = serializers.SerializerMethodField()

    def get_liked_count(self,post):
        return Like.objects.filter(post_id=post.id).count()

    class Meta:
        model = Post
        fields = '__all__'
