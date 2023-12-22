from django.db import models

# Create your models here.


class UploadImage(models.Model):
    upload = models.ImageField(upload_to="images/")

    @property
    def url(self):
        return self.upload.url
