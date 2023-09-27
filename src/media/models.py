from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Video(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    image = models.ImageField(upload_to='Images/Blog')
    created_on = models.DateField(blank=True, null=True, verbose_name="Date")
    published = models.BooleanField(default=False, verbose_name="Publié")
    lien = models.TextField(blank=True, verbose_name="lien de la vidéo youtube")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Vidéo"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)


class Actualite(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")


    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Actualité"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)




class ImagesActualite(models.Model):
    actualite = models.ForeignKey(Actualite, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/Blog/ImagesByActu', verbose_name='Images de l\'actuaité')
