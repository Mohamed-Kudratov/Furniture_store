# Generated by Django 3.2.6 on 2021-08-29 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210827_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='color')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
        ),
        migrations.AddField(
            model_name='productmodel',
            name='colors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.colormodel', verbose_name='colors'),
        ),
    ]