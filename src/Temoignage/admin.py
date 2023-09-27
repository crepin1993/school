from django.contrib import admin
from Temoignage.models import Temoignage



@admin.register(Temoignage)
class CoursAdmin(admin.ModelAdmin):
    list_display = ("fullname", "image",  "published", "slug", "content", )
    list_editable = ("published",)
    search_fields = ("fullname", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = Temoignage