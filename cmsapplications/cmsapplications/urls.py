"""
URL configuration for cmsapplications project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include

api_v1_urls = [
    re_path("account/", include("apps.account.api_v1.urls", namespace="v1-accounts")),
    re_path("cmsapp/", include("apps.cmsapp.api_v1.urls", namespace="v1-cmsapp")),
]

urlpatterns = [
    re_path('admin/', admin.site.urls),
    re_path('api_v1/',include(api_v1_urls))
]