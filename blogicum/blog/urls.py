from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CustomLoginView
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.index, name='index'),
    path('musics/<int:music_id>/', views.music_detail, name='music_detail'),
    path('musics/<int:music_id>/like/', views.add_like, name='add_like'),
    path('performer/<slug:performer_slug>/', views.performer_music,
         name='performer_music'),
    path('album/<slug:album_slug>/', views.music_album,
         name='music_album'),
    path('genre/<slug:genre_slug>/', views.music_genre,
         name='music_genre'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('auth/registration/', views.registration, name='registration'),
    path('auth/password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change_form.html'
         ),
         name='password_change'),
    path('auth/password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'
         ),
         name='password_change_done'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/<str:username>/', views.profile, name='profile'),

]
