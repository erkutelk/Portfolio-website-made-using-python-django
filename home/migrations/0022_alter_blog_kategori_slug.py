# Generated by Django 4.2.9 on 2024-09-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_blog_slug_alter_blog_kategori_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_kategori',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
