# Generated by Django 5.2.4 on 2025-08-01 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0005_image"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Image",
            new_name="images",
        ),
    ]
