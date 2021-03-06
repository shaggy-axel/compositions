from django.db import models
from django.core.validators import FileExtensionValidator


class Anime(models.Model):
    composition = models.ForeignKey(
        'compositions.Composition', on_delete=models.CASCADE,
        verbose_name="Composition"
    )
    
    def __str__(self):
        return self.composition.name

    @property
    def season_amount(self):
        return max([season.number for season in self.anime_seasons.all()])

    class Meta:
        verbose_name_plural = "Anime"


class AnimeSeason(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Anime Season Number"
    )
    anime = models.ForeignKey(
        Anime, on_delete=models.CASCADE, verbose_name="Anime",
        related_name="anime_seasons",
    )

    @property
    def name(self):
        return self.anime.composition.name


class AnimeSeries(models.Model):
    number = models.PositiveSmallIntegerField(
        verbose_name="Anime Series Number"
    )
    name = models.CharField(max_length=120, verbose_name='Series Name')
    description = models.TextField(verbose_name='Description of the Series')
    season = models.ForeignKey(
        AnimeSeason, on_delete=models.CASCADE, verbose_name="Anime Season",
    )


class AnimeVideo(models.Model):
    video = models.FileField(upload_to='anime', validators=[
        FileExtensionValidator(
            allowed_extensions=[
                'MOV', 'avi', 'mp4', 'webm', 'mkv'
            ]
        )
    ], verbose_name="Video")
    series = models.ForeignKey(
        AnimeSeries, on_delete=models.CASCADE, verbose_name="Anime Series"
    )
