# Generated by Django 4.2.9 on 2024-09-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_portfoy_project_portfoykategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfoy_project',
            name='portfoyKategori',
        ),
        migrations.AddField(
            model_name='portfoy_project',
            name='categories',
            field=models.ManyToManyField(related_name='projects', to='home.portfoy_kategori'),
        ),
    ]
