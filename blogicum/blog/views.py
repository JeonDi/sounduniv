from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Music, Performer, Album, Genre, MusicLike
from .forms import UserEditForm
from django.utils import timezone
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.paginator import Paginator
from django.urls import reverse


class CustomLoginView(LoginView):
    def get_success_url(self):
        kwargs = {'username': self.request.user.username}
        return reverse('profile', kwargs=kwargs)


def index(request):
    musics = Music.objects.all().filter(
        year__lte=2024,
    ).order_by('-year')
    paginator = Paginator(musics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/index.html', {'page_obj': page_obj})


def music_detail(request, music_id):
    music = get_object_or_404(Music, id=music_id)
    if music.year > 2024:
        raise Http404()
    context = {
        'music': music,
    }
    return render(request, 'blog/detail.html', context)


def performer_music(request, performer_slug):
    performer = get_object_or_404(
        Performer,
        slug=performer_slug,
    )
    musics = Music.objects.all().filter(
        performer=performer,
        year__lte=2024
    ).order_by('-year')
    paginator = Paginator(musics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'performer': performer,
    }
    return render(request, 'blog/performer.html', context)


def music_album(request, album_slug):
    album = get_object_or_404(
        Album,
        slug=album_slug,
    )
    musics = Music.objects.all().filter(
        album=album,
        year__lte=2024
    ).order_by('-year')
    paginator = Paginator(musics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'album': album,
    }
    return render(request, 'blog/album.html', context)


def music_genre(request, genre_slug):
    genre = get_object_or_404(
        Genre,
        slug=genre_slug,
    )
    musics = Music.objects.all().filter(
        genre=genre,
        year__lte=2024
    ).order_by('-year')
    paginator = Paginator(musics, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'genre': genre,
    }
    return render(request, 'blog/genre.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('blog:index')
    else:
        form = UserCreationForm()
    return render(request,
                  'registration/registration_form.html',
                  {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)
    likes = MusicLike.objects.all().filter(user=user)
    paginator = Paginator(likes, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'user': request.user,
        'profile': user,
        'page_obj': page_obj,
    }
    return render(request, 'blog/profile.html', context)


@login_required
def edit_profile(request):
    user = get_object_or_404(User, id=request.user.id)
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = UserEditForm(instance=user)
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'blog/user.html', context)


@login_required
def add_like(request, music_id):
    music = Music.objects.get(id=music_id)
    user = request.user
    like, created = MusicLike.objects.get_or_create(music=music, user=user)
    if not created:
        like.like = not like.like
    like.save()
    return redirect('music_detail', music_id=music_id)

