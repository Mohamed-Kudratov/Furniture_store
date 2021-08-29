# Generated by Django 3.2.6 on 2021-08-26 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='image',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image_first',
            field=models.ImageField(null=True, upload_to='products', verbose_name='image first'),
        ),
        migrations.AddField(
            model_name='productmodel',
            name='image_second',
            field=models.ImageField(null=True, upload_to='products', verbose_name='image second'),
        ),
    ]
