from django.contrib import admin
from presentation.models import Partenaire, Formateur, Administration, DirectionGenerale, Statistique, Cours


@admin.register(Partenaire)
class PartenaireAdmin(admin.ModelAdmin):

    list_display = ("libelle", "published", "slug", "lien")
    list_editable = ("lien",)
    search_fields = ("libelle", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Partenaire


@admin.register(Formateur)
class FormateurAdmin(admin.ModelAdmin):
    list_display = ("fullname", "cv", "grade", "resume", "published")
    list_editable = ("published",)
    search_fields = ("fullname", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Formateur


@admin.register(Administration)
class AdministrationAdmin(admin.ModelAdmin):
    list_display = ("fullname", "cv", "grade", "resume", "published")
    list_editable = ("published",)
    search_fields = ("fullname", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Administration

@admin.register(DirectionGenerale)
class DirectionGeneraleAdmin(admin.ModelAdmin):
    list_display = ("fullname", "cv", "grade", "resume", "published", "mot_dg")
    list_editable = ("published",)
    search_fields = ("fullname", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = DirectionGenerale

@admin.register(Statistique)
class StatistiqueAdmin(admin.ModelAdmin):
    list_display = ("titre", "nombre",  "published")
    list_editable = ("published",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Statistique

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ("titre", "fichier",  "published", "slug", )
    list_editable = ("published",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Cours