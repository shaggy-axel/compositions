# Generated by Django 4.0.5 on 2022-07-01 17:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('compositions', '0003_alter_composition_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compositions.composition', verbose_name='Composition')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Anime Season Number')),
                ('anime', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.anime', verbose_name='Anime')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveSmallIntegerField(verbose_name='Anime Series Number')),
                ('name', models.CharField(max_length=120, verbose_name='Series Name')),
                ('description', models.TextField(verbose_name='Description of the Series')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.animeseason', verbose_name='Anime Season')),
            ],
        ),
        migrations.CreateModel(
            name='AnimeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='anime', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])], verbose_name='Video')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anime.animeseries', verbose_name='Anime Series')),
            ],
        ),
    ]
