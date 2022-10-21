# Generated by Django 3.2.6 on 2022-10-21 14:29

import django.core.files.storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0002_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='playlist',
            fields=[
                ('id_playlist', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('images_list', models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(base_url='media/'), upload_to='playlist/')),
                ('director', models.CharField(max_length=100)),
                ('writer', models.CharField(max_length=100)),
                ('network', models.CharField(max_length=100)),
                ('episodes', models.CharField(max_length=100)),
                ('release_date', models.CharField(max_length=100)),
                ('runtime', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('id_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idcategory', to='category.category')),
                ('id_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='idgenre', to='category.genre')),
            ],
        ),
    ]
