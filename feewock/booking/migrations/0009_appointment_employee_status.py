# Generated by Django 4.2.10 on 2024-02-18 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_alter_appointment_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='employee_status',
            field=models.CharField(choices=[('coming', 'Coming'), ('on_the_way', 'On the Way'), ('nearest', 'Nearest')], default='coming', max_length=10, null=True),
        ),
    ]
