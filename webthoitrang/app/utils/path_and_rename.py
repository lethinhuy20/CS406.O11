from uuid import uuid4
import os


def generate_name(instance, filename):
    """Generate new name using uuid for an uploaded image"""
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join('uploaded-images/', filename)



