# Generated by Django 4.2.10 on 2024-02-14 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_reviews_star_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]