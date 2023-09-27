from django.shortcuts import render

from scolarite.models import EmploiDuTemps, Actualite, Classe


def index(request):
    classes = Classe.objects.filter(published=True)
    actualites= Actualite.objects.filter(published=True)
    template_name = "scolarite/index.html"
    return render(request, template_name, context={"classes": classes, "actualites":actualites})
