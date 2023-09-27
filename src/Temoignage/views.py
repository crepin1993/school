from django.shortcuts import render
from Temoignage.models import Temoignage

def AllTemoignage():
    temoignages=Temoignage.objects.filter(published=True)
    return temoignages