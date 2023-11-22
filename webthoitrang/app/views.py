from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UploadFile
# Create your views here.
def home(request):
    #return render(request,'app/home.html')
    return render(request,'for20/home.html')
def result(request):
    context = None
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        print(1111111111)
        context = {'search_image': my_file}
    return render(request,'for20/index.html', context)

def file_upload_view(request):
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        uploaded_file = UploadFile.objects.create(upload=my_file)
        url = 'http://127.0.0.1:8000/upload/'+uploaded_file.upload.name.split('/')[-1]
        context = {'search_image': url}
        print(111111111111111)
        return render(request, 'for20/index.html', context)
    return JsonResponse({'post:':'false'})