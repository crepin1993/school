from django.shortcuts import render
from presentation.models import Partenaire, Formateur, Administration, DirectionGenerale, Statistique, Cours

def index(request):
    dg= DirectionGenerale.objects.last()
    formateurs=Formateur.objects.filter(published=True)
    cours = Cours.objects.filter(published=True)
    partenaires=Partenaire.objects.filter(published=True)
    administrations=Administration.objects.filter(published=True)
    stats=Statistique.objects.filter(published=True)


    return render(request, "presentation/index.html", context={"dg":dg,"cours":cours, "formateurs":formateurs, "partenaires": partenaires, "administrations":administrations, "stats":stats})
