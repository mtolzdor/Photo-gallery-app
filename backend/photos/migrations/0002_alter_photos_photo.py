# Generated by Django 4.0.5 on 2022-06-17 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
