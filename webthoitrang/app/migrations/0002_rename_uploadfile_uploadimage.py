# Generated by Django 4.2.7 on 2023-12-21 03:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="UploadFile",
            new_name="UploadImage",
        ),
    ]
