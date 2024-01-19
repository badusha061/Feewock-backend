# Generated by Django 5.0.1 on 2024-01-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0008_alter_usermodel_location_alter_usermodel_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='role',
            field=models.IntegerField(choices=[(1, 'ADMIN'), (2, 'EMPLOYEE'), (3, 'USER')], default=3),
        ),
    ]