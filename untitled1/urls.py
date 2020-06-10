"""untitled1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.generics import ListCreateAPIView
from rest_framework.routers import DefaultRouter
from practice import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'candidates', views.CandidateViewSet, basename="candidates")
router.register(r'vote', views.VoteViewSet, basename="vote")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]

"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list),
    path('candidates/', views.candidate_list)
]
"""