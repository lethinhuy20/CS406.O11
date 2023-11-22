from django.contrib import admin
from django.urls import path
from . import views
# from app.views import file_upload_view
urlpatterns = [
    path('', views.home),
    path('result/', views.result),
    path('upload/',views.file_upload_view),
    # path('upload/',file_upload_view)
]