from django.shortcuts import render

from media.models import Video, Actualite


def index(request):
    videos = Video.objects.filter(published=True)
    actualites= Actualite.objects.filter(published=True)
    template_name = "media/index.html"
    return render(request, template_name, context={"videos": videos, "actualites":actualites})
