from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadImage


# Create your views here.
def home(request):
    return render(request, "app/home.html")


def file_upload_view(request):
    if request.method == "POST":
        uploaded_image = request.FILES.get("file")
        query_image = UploadImage.objects.create(upload=uploaded_image)
        return JsonResponse({"url": "/result/{}".format(query_image.id)})
    return JsonResponse({"post": "false"})


def result(request, pk):
    query_image = UploadImage.objects.get(id=pk)
    ###PERFORM IMAGE SEARCH HERE###
    # Your code here...
    # result_urls = [...] # The result images' urls should be placed in here
    # Example:
    result_urls = [
        "products/somitrang.jpeg",
        "products/somitrang.jpeg",
        "products/somitrang.jpeg",
        "products/somitrang.jpeg",
        "products/somitrang.jpeg",
    ]
    # Note that the urls should be exact the ones that are in your .csv file
    ###############################
    return render(
        request,
        "app/home.html",
        {"query_image": query_image, "result_urls": result_urls},
    )
