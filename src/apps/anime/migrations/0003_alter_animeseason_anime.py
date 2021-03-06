# Generated by Django 4.0.5 on 2022-07-01 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0002_alter_anime_options_alter_animeseason_anime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animeseason',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_seasons', to='anime.anime', verbose_name='Anime'),
        ),
    ]
