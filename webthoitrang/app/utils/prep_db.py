import csv, re, os 
from django.db import transaction
from app.models import DatabaseImage

if __name__ == '__main__':
    path_pattern = re.compile('(\d+)_([A-Z]+)_([a-zA-Z_]+)_\d+_\d+_\d_([a-z]+)')

    print('======ADDING INFORMATION TO THE DATABASE========')
    with open('app/faiss_retrieval/indexes/image_index.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Extract category and gender from filename
            _, gender, category, _ = path_pattern.search(row['Filename']).groups()

            # Create and save model instance
            with transaction.atomic():
                model_instance = DatabaseImage.objects.create(
                    index=row['Index'],
                    url=row['Filename'],
                    category=category,
                    gender=gender
                )
    print('======DONE INFORMATION TO THE DATABASE========')
    exit()