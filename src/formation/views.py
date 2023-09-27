from django.shortcuts import render

from formation.models import Formation, Filiere, ModaliteInscription


def index(request):
    filieres = Filiere.objects.filter(published=True)
    template_name = "formation/index.html"

    return render(request, template_name, context={"filieres":filieres})

def DetailFormationView(request,slug):
    filiere = Filiere.objects.get(slug=slug)
    formations=Formation.objects.filter(filiere=filiere)
    modalites=ModaliteInscription.objects.filter(filiere=filiere)

    template_name = "formation/detail.html"
    return render(request, template_name, context={"formations": formations, "filiere":filiere, "modalites":modalites})

