# Generated by Django 5.0.1 on 2024-02-06 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeProfile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeesavailability',
            name='date',
            field=models.DateField(unique=True),
        ),
    ]