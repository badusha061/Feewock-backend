# Generated by Django 5.0.1 on 2024-01-11 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_auth', '0010_alter_employees_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='otp',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
