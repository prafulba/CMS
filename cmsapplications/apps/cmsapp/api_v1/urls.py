from apps.cmsapp.api_v1 import views
from rest_framework import routers
from django.urls import re_path

router = routers.SimpleRouter()
router.register("post", views.PostAPIViewSet)
router.register("like-unlike", views.LikeViewSet)


app_name = "cmsapp"

urlpatterns = [
    re_path('api_v1/cmsapp/like-unlike/<int:pk>/unlike/', views.LikeViewSet.as_view({'post': 'unlike'}), name='like-unlike-unlike'),
]  + router.urls