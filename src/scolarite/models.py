from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Classe(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé de la classe")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-libelle']  # les derniers publiés en premiers
        verbose_name = "Classe"

    def __str__(self):
        return self.libelle

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.libelle)
            # ex "Un libelle" le slugify fera "un-libelle"
        super().save(*args)


class EmploiDuTemps(models.Model):
    classe = models.ForeignKey(Classe,on_delete=models.SET_NULL, null=True)
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    fichier = models.FileField(upload_to='Scolarite/EmploisDuTemps/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")


    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Emploie du temps"

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
    fichier = models.FileField(upload_to='Scolarite/Actualite/', blank=True, null=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Autre actualité"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)