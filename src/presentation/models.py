from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Partenaire(models.Model):
    libelle = models.CharField(max_length=255, unique=True, verbose_name="Libellé ")
    lien = models.CharField(max_length=255, verbose_name="Lien ou page du partenaire", null=True, blank=True)
    image = models.ImageField(upload_to='Presentation/Partenaire/Image/', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-libelle']  # les derniers publiés en premiers
        verbose_name = "Partenaire"

    def __str__(self):
        return self.libelle

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.libelle)
            # ex "Un libelle" le slugify fera "un-libelle"
        super().save(*args)


class Formateur(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Nom & Prenom")
    cv = models.FileField(upload_to='Presentation/Formateur/CV/', blank=True, null=True)
    image = models.ImageField(upload_to='Presentation/Formateur/Image/', blank=True, null=True)
    grade = models.CharField(max_length=255, verbose_name="Grade")
    resume = models.TextField(max_length=255, verbose_name="résumé sur le formateur", null=True, blank=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")


    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Formateur"

    def __str__(self):
        return self.fullname

class Administration(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Nom & Prenom")
    cv = models.FileField(upload_to='Presentation/Admin/CV/', blank=True, null=True)
    image = models.ImageField(upload_to='Presentation/Admin/Image/', blank=True, null=True)
    grade = models.CharField(max_length=255, verbose_name="Grade")
    resume = models.TextField(max_length=255, verbose_name="résumé sur le formateur", null=True, blank=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")


    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Administration"

    def __str__(self):
        return self.fullname

class DirectionGenerale(models.Model):
    fullname = models.CharField(max_length=255, verbose_name="Nom & Prenom")
    cv = models.FileField(upload_to='Presentation/DG/CV/', blank=True, null=True)
    image = models.ImageField(upload_to='Presentation/DG/Image/', blank=True, null=True)
    grade = models.CharField(max_length=255, verbose_name="Grade")
    resume = models.TextField(max_length=255, verbose_name="résumé sur le formateur", null=True, blank=True)
    mot_dg = models.TextField(max_length=255, verbose_name="Le mot du chef", null=True, blank=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")


    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "DirectionGenerale"

    def __str__(self):
        return self.fullname




class Statistique(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    fichier = models.FileField(upload_to='presentation/Statistique/', blank=True, null=True)
    nombre = models.IntegerField(blank=True, null=True,  verbose_name="Chiffre")
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        verbose_name = "Les statistiques"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)


class Cours(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='Presentation/Cours/Image/', blank=True, null=True)
    fichier = models.FileField(upload_to='Presentation/Cours/Fichier/', blank=True, null=True)
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Les cour"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)