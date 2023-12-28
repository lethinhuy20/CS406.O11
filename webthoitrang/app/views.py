from django.shortcuts import render
from django.http import JsonResponse
from .models import UploadImage, DatabaseImage
from .faiss_retrieval.faiss_index import load_index, query_index
from .faiss_retrieval.features import extract_CLIP_features



# Create your views here.
def home(request):
    return render(request, "app/home.html")


def file_upload_view(request):
    if request.method == "POST":
        uploaded_image = request.FILES.get("file")
        query_image = UploadImage.objects.create(upload=uploaded_image)
        print(query_image.upload.path)
        return JsonResponse({"url": "/result/{}".format(query_image.id)})
    return JsonResponse({"post": "false"})


def result(request, pk):
    """Retrieves similar images based on a query image."""
    query_image = UploadImage.objects.get(id=pk)
    ###PERFORM IMAGE SEARCH HERE###
    # Load the FAISS index
    # index_path = "faiss_retrieval/indexes/fclip_B32_full_index.bin"
    # index = load_index(index_path)

    # # Extract features from the query image
    # query_features = extract_CLIP_features(request.data["image_path"])

    # # Query the index for similar images
    # _, indices = query_index(index, query_features)  # Retrieve 5 nearest neighbors
    # top_10_indices = indices[0]

    # Retrieve image data and metadata based on indices
    # similar_images = Image.objects.filter(id__in=indices)
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
        context={
            "query_image": query_image, 
            "result_urls": result_urls
            },
    )