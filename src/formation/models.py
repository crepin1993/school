from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Filiere(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    image = models.ImageField(upload_to='Images/Blog')
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Filière"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)

    def get_absolute_url(self):
        pass
        #return reverse("blog-post", kwargs={"slug":self.slug})


class Formation(models.Model):
    filiere = models.ForeignKey(Filiere, default=None, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='Images/Formations/ImagesFormation', verbose_name='Images de l\'actuaité', blank=True,
                              null=True)
    class Meta:
        ordering = ['-titre']
        verbose_name = "Formation"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)

    def get_absolute_url(self):
        pass

class Option(models.Model):
    formation = models.ForeignKey(Formation, default=None, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='Images/Formations/ImagesFormation', verbose_name='Images de la formation', blank=True,
                              null=True)

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)

class ModaliteInscription(models.Model):
    filiere = models.ForeignKey(Filiere, default=None, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)


    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)