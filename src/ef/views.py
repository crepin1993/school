from django.shortcuts import render

from django.views import View
from django.views.generic import TemplateView

from blog.models import BlogPost
from formation.models import Filiere
from media.models import Actualite
from presentation.models import Statistique, Partenaire, Administration
from Temoignage.views import AllTemoignage


# vues fondées sur les classes
def index(request):
    filieres = Filiere.objects.filter(published=True)
    stats=Statistique.objects.filter(published=True)
    partenaires=Partenaire.objects.filter(published=True)
    administrations = Administration.objects.filter(published=True)
    actualites = Actualite.objects.filter(published=True)
    blogs = BlogPost.objects.filter(published=True).order_by("id")[:3]
    temoignages=AllTemoignage()

    template_name= "ef/index.html"
    return render(request,template_name,
                  context={"filieres":filieres, "stats":stats,
                           "partenaires": partenaires, "administrations": administrations,
                           "actualites":actualites, "blogs": blogs, "temoignages":temoignages})




"""
vues par function
def index(request):
    return render(request,"ef/index.html")
    
"""