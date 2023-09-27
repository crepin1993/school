from django.contrib import admin
from formation.models import Filiere, Formation, Option, ModaliteInscription


# Register your models here.
@admin.register(Filiere)
class FiliereAdmin(admin.ModelAdmin):
    list_display = ("titre", "published", "created_on","slug", "last_updated", "image")
    list_editable = ( "titre", "published", "image", )
    list_display_links = ("created_on", ) # colonne sur laquelle on va cliquer
    ordering = ["-created_on"]
    empty_value_display="Aucune valeur" # champ contenant une valeur nulle
    search_fields = ("filiere",)

@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ("titre", "slug", "filiere", )
    autocomplete_fields = ("filiere", )
    empty_value_display = "Aucune information"


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ("titre", "formation", "slug", )
    list_editable = ("titre", )
    list_display_links = ("formation",)


@admin.register(ModaliteInscription)
class ModaliteInscriptionAdmin(admin.ModelAdmin):
    list_display = ("titre", "filiere", "slug", )
    list_editable = ("titre", )
    list_display_links = ("slug",)
