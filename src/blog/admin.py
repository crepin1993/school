from django.contrib import admin

from blog.models import BlogPost, ImagesActualite

"""class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("titre", "published", "created_on", "last_updated", "lieu")
    list_editable = ("published", )

admin.site.register(BlogPost, BlogPostAdmin)
"""


class ImagesActualiteAdmin(admin.StackedInline):
    model = ImagesActualite


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):

    inlines = [ImagesActualiteAdmin]
    list_display = ("titre", "published", "created_on", "last_updated", "lieu")
    list_editable = ("published",)
    search_fields = ("titre", ) # barre de recherche ( on cherche par titre )
    list_filter = ("published", ) # filtrer pour voir ceux qui sont publiés ou pas
    class Meta:
        model = BlogPost


"""@admin.register(ImagesActualiteAdmin)
class ImagesActualiteAdmin(admin.ModelAdmin):
    pass"""
