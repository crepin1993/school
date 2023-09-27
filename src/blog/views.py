from django.shortcuts import render
from django.views.generic import ListView,DetailView

from blog.models import BlogPost,ImagesActualite


def BlogIndexView(request):
    blogs = BlogPost.objects.filter(published=True)
    template_name = "blog/index.html"

    return render(request, template_name, context={"blogs":blogs})

def DetailActualiteView(request,slug):
    blog = BlogPost.objects.get(slug=slug)
    template_name = "blog/detail.html"
    images=blog.imagesactualite_set.all()

    return render(request, template_name, context={"blog":blog, "images":images})




"""def index(request):
    return render(request, "blog/index.html")"""
