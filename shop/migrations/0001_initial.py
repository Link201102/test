# Generated by Django 5.1.5 on 2025-02-22 07:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250, verbose_name='type')),
                ('country', models.CharField(max_length=250, verbose_name='country')),
                ('model', models.CharField(max_length=250, verbose_name='model')),
                ('code', models.CharField(max_length=250, verbose_name='code')),
                ('year', models.CharField(max_length=250, verbose_name='year')),
                ('material', models.CharField(max_length=250, verbose_name='material')),
                ('color', models.CharField(max_length=250, verbose_name='color')),
                ('size', models.CharField(max_length=250, verbose_name='size')),
                ('weight', models.CharField(max_length=250, verbose_name='weight')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=250, verbose_name='category_name')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='shop.category')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'unique_together': {('slug', 'parent')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Product')),
                ('price', models.FloatField(verbose_name='Price')),
                ('slug', models.SlugField(max_length=250, unique=True, verbose_name='URL')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('Characteristics', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.characteristics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.category')),
            ],
        ),
    ]
