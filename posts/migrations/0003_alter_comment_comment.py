# Generated by Django 4.2 on 2023-06-05 09:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0002_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="comment",
            field=models.CharField(max_length=100),
        ),
    ]
