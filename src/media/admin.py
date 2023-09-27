from django.contrib import admin
from media.models import Video, ImagesActualite,Actualite


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = ("titre", "published", "created_on", "last_updated", "lien")
    list_editable = ("lien",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Video

class ImagesActualiteAdmin(admin.StackedInline):
    model = ImagesActualite


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):

    inlines = [ImagesActualiteAdmin]
    list_display = ("titre", "published", "created_on", "last_updated")
    list_editable = ("published",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Actualite
