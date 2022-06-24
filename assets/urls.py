from django.urls import path

from assets.views import home

urlpatterns = [path("", home)]
