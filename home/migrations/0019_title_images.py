# Generated by Django 4.2.9 on 2024-09-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_blog_kategori_remove_portfoy_project_categories_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='images',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
