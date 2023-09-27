from django.contrib import admin
from scolarite.models import Classe, EmploiDuTemps,Actualite


@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):

    list_display = ("libelle", "published", "slug",)
    list_editable = ("libelle",)
    list_display_links = ("slug",)
    search_fields = ("libelle", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Classe


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):

    list_display = ("titre", "published", "created_on", "slug", "fichier", )
    list_editable = ("titre", "published", )
    list_display_links = ("slug",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Actualite


@admin.register(EmploiDuTemps)
class EmploiDuTempsAdmin(admin.ModelAdmin):

    list_display = ("titre", "published", "classe", "created_on",  "slug", "fichier",  )
    list_editable = ("titre", "published", )
    list_display_links = ("slug",)
    search_fields = ("classe", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas

    class Meta:
        model = EmploiDuTemps