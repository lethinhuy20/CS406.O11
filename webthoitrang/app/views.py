from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import UploadFile
# Create your views here.
def home(request):
    #return render(request,'app/home.html')
    return render(request,'home/index.html')

def file_upload_view(request):
    #print(request.FILES)
    if request.method == 'POST':
        my_file = request.FILES.get('file')
        UploadFile.objects.create(upload=my_file)
        return HttpResponse('')
    return JsonResponse({'post:':'false'})