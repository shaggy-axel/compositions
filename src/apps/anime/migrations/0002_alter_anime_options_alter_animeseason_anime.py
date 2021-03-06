# Generated by Django 4.0.5 on 2022-07-01 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anime',
            options={'verbose_name_plural': 'Anime'},
        ),
        migrations.AlterField(
            model_name='animeseason',
            name='anime',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anime_season', to='anime.anime', verbose_name='Anime'),
        ),
    ]
