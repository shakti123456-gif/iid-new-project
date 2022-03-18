from django.contrib import admin
from django.urls import path, include

from .views import ArticleListview, ModelNameDetail

app_name = 'Blog'

urlpatterns = [

    path('',ArticleListview.as_view(),name="list_view"),


]


