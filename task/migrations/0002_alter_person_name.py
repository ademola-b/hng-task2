# Generated by Django 4.2.5 on 2023-09-13 05:43

from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=50, unique=True, validators=[task.models.validate_no_numbers]),
        ),
    ]
