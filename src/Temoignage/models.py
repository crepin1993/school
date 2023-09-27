from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Temoignage(models.Model):
    fullname = models.CharField(max_length=255, unique=True, verbose_name="Nom & prenom de l'étudiant ")
    content = models.TextField(max_length=255, verbose_name="Commentaire")
    image = models.ImageField(upload_to='Temoignage/Image/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-fullname']  # les derniers publiés en premiers
        verbose_name = "Temoignage"

    def __str__(self):
        return self.fullname

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.fullname)
            # ex "Un libelle" le slugify fera "un-libelle"
        super().save(*args)


