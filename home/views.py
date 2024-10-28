from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.template.loader import render_to_string
from home.sitemaps import StaticViewSitemap
from django.contrib.sitemaps.views import sitemap as django_sitemap



def index(request):

    """ A view to return the index page """

    meta_description = "Welcome to Smart Tech, your go-to place for the latest tech gadgets and accessories."
    context = {
        'meta_description': meta_description,
    }

    return render(request,'home/index.html')

def sitemap(request: HttpRequest):
    return django_sitemap(request, sitemaps)

def robots_txt(request):
    return HttpResponse("User-agent: *\nDisallow: /admin/\nDisallow: /private/\n\nSitemap: https://smart-tech-42a1ef4a43e4.herokuapp.com/sitemap.xml", content_type="text/plain")