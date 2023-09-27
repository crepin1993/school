from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class BlogPost(models.Model):
    titre = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    lieu = models.CharField(max_length=255, blank=True, null=True, verbose_name="Lieu")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True, verbose_name="Dernière mise à jour")
    image = models.ImageField(upload_to='Images/Blog')
    created_on = models.DateField(blank=True, null=True, verbose_name="Date de création")
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")

    # ordre dans lequel les articles vont être affichés dans l'interface d'administration
    class Meta:
        ordering = ['-created_on']  # les derniers publiés en premiers
        verbose_name = "Article"

    def __str__(self):
        return self.titre

    def save(self, *args, **kwargs):
        if not self.slug:  # si on n'a pas de slug
            self.slug = slugify(self.titre)
            # ex "Un titre" le slugify fera "un-titre"
        super().save(*args)

    def get_absolute_url(self):
        return reverse("blog-post", kwargs={"slug":self.slug})


class ImagesActualite(models.Model):
    post = models.ForeignKey(BlogPost, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Images/Blog/ImagesByActu', verbose_name='Images de l\'actuaité')
