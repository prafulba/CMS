from django.urls import re_path
from rest_framework import routers
from apps.account.api_v1 import views

app_name = "account"

urlpatterns = [
    re_path(r'create-account/$', views.RegisterUserAPIView.as_view()),
    re_path(r'login/$', views.LoginUserAPIView.as_view()),
    re_path(r'profile/$', views.UserProfileAPIView.as_view()),
    re_path(r'update-profile/$', views.UpdateProfileAPIView.as_view()),
    re_path(r'change-password/$', views.UserChangePasswordAPIView.as_view()),
]