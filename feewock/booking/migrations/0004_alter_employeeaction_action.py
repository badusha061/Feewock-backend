# Generated by Django 5.0.1 on 2024-02-07 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_appointment_user_alter_appointment_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeaction',
            name='action',
            field=models.CharField(choices=[('accepted', 'Accepted'), ('rejected', 'Rejected'), ('pending', 'Pending')], max_length=50),
        ),
    ]