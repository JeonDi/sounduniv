from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


User = get_user_model()


class Music(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name="Название"
    )
    performer = models.ForeignKey(
        'Performer',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Исполнитель"
    )
    album = models.ForeignKey(
        'Album',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Альбом"
    )
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Жанр"
    )
    year = models.PositiveIntegerField(
        verbose_name="Год"
    )
    duration = models.CharField(
        max_length=10,
        verbose_name="Продолжительность"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "композиция"
        verbose_name_plural = "Композиции"


class Performer(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=("Название")
    )
    description = models.TextField(
        blank=True,
        verbose_name=("Описание")
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=("Идентификатор")
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name=("Изображение")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("автор")
        verbose_name_plural = ("Авторы")


class Album(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=("Название")
    )
    performer = models.ForeignKey(
        'Performer',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name=("Исполнитель")
    )
    year = models.PositiveIntegerField(
        verbose_name=("Год")
    )
    description = models.TextField(
        blank=True,
        verbose_name=("Описание")
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=("Идентификатор")
    )
    image = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
        verbose_name=("Изображение")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("альбом")
        verbose_name_plural = ("Альбомы")


class Genre(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name=("Название")
    )
    description = models.TextField(
        blank=True,
        verbose_name=("Описание")
    )
    slug = models.SlugField(
        unique=True,
        verbose_name=("Идентификатор")
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("жанр")
        verbose_name_plural = ("Жанры")


class MusicLike(models.Model):
    music = models.ForeignKey(Music, on_delete=models.SET_NULL, null=True, verbose_name='Композиция')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Автор')
    like = models.BooleanField('Like', default=False)
    created = models.DateTimeField('Дата и время', default=timezone.now)

    def __str__(self):
        return f'{self.user}: {self.music} {self.like}'

    class Meta:
        verbose_name = ("лайк")
        verbose_name_plural = ("Лайки")