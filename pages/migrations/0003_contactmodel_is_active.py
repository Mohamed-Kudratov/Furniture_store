# Generated by Django 3.2.6 on 2021-08-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_bannermodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmodel',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is active'),
        ),
    ]
