from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from app.views import file_upload_view
urlpatterns = [
    path("", views.home, name="home"),
    path("result/<str:pk>", views.result, name="result"),
    path("upload/", views.file_upload_view, name="upload"),
]
