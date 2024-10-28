from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['home', 'products', 'view_bag', 'checkout', 'profile', 'contact', 'subscribe', 'faq']

    def location(self, item):
        return reverse(item)

    def get_absolute_url(self, request):
        return request.build_absolute_uri(self.location(item))
