# Generated by Django 5.0.7 on 2024-07-17 14:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_car_delete_product"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="student",
            name="file",
        ),
        migrations.RemoveField(
            model_name="student",
            name="image",
        ),
    ]
