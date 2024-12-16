from django.contrib import admin
from .models import Music, Performer, Album, Genre, MusicLike


class MusicAdmin(admin.ModelAdmin):
    list_display = ('name', 'performer', 'album', 'genre', 'year', 'duration')
    list_filter = ('name', 'performer', 'album', 'genre')
    search_fields = ('name', 'performer', 'album', 'genre')

class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ('name', )


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'performer', 'year', 'description', 'slug')
    search_fields = ('name', )


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    search_fields = ('name',)


class MusicLikeAdmin(admin.ModelAdmin):
    autocomplete_fields = ('user', 'music')
    list_display = ('music', 'user', 'like', 'created')


admin.site.register(Music, MusicAdmin)
admin.site.register(Performer, PerformerAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MusicLike, MusicLikeAdmin)
