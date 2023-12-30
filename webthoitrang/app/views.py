from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadImage, DatabaseImage
from .faiss_retrieval.faiss_index import load_index, query_index
from .faiss_retrieval.features import extract_CLIP_features
import os 
from pathlib import Path
import time


CURRENT_DIR = Path(__file__).resolve().parent
BASE_DIR = Path(__file__).resolve().parent.parent



# Create your views here.
def home(request):
    return render(request, "app/home.html")


def file_upload_view(request):
    if request.method == "POST":
        try: 
            uploaded_image = request.FILES.get("file")
            query_image = UploadImage.objects.create(upload=uploaded_image)
            return JsonResponse({"url": "/result/{}".format(query_image.id)})
        except Exception as e: 
            return JsonResponse({
                "post": "false",
                "error": e,
            })
        


def result(request, pk):
    """Retrieves similar images based on a query image."""
    if request.method == 'GET':
        try:
            start_time = time.time()
            query_image = UploadImage.objects.get(id=pk)
            # Load the FAISS index
            index_path = os.path.join(CURRENT_DIR, "faiss_retrieval/indexes/fclip_B32_full_index.bin")
            index = load_index(index_path)
            # Extract features from the query image
            retrieve_path = os.path.join(BASE_DIR, query_image.url[1:])
            query_features = extract_CLIP_features(retrieve_path)
            # Query the index for similar images
            _, indices = query_index(index, query_features)  # Retrieve 5 nearest neighbors
            top_5_indices = indices[0]
            print(top_5_indices)

            # Retrieve image data and metadata based on indices by mapping indices to the media database
            retrieved_objects = DatabaseImage.objects.filter(index__in=top_5_indices)
            host = request.get_host()
            results = []
            for obj in retrieved_objects:
                result_url = os.path.join(host,'/media', obj.url)
                results.append((result_url, obj.category, obj.gender))  # Access model fields
            print(results)
            end_time = time.time()
            process_time = end_time - start_time
            print("Thời gian tìm kiếm: {:.2f} giây".format(process_time))
            with open('LOG_SEARCH_TIME.txt', 'a') as log:
                log.write(f'\n{retrieve_path}, {process_time}, {top_5_indices}, {results}')
            return render(
                request,
                "app/home.html",
                context={
                    "query_image": query_image, 
                    "results": results,
                },
            )
        except Exception as e: 
            print(e)
            return render(
                request,
                'app/home.html',
                context={
                    "err": e,
                }
            ) 
    