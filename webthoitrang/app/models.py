from django.db import models
from .utils.path_and_rename import generate_name
# Create your models here.



class UploadImage(models.Model):
    upload = models.ImageField(upload_to=generate_name)

    @property
    def url(self):
        return self.upload.url


class DatabaseImage(models.Model):
    index = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    url = models.URLField(max_length=200)
    category = models.CharField(max_length=50)  # Adjust max_length as needed
    gender = models.CharField(max_length=10)  # Assuming limited gender options