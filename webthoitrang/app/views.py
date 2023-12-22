from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadImage


# Create your views here.


def home(request):
    return render(request, "app/home.html")


def result(request, pk):
    query_image = UploadImage.objects.get(id=pk)
    return render(request, "app/home.html", {"query_image": query_image})


def file_upload_view(request):
    if request.method == "POST":
        uploaded_image = request.FILES.get("file")
        query_image = UploadImage.objects.create(upload=uploaded_image)
        return JsonResponse({"url": "/result/{}".format(query_image.id)})
    return JsonResponse({"post": "false"})
