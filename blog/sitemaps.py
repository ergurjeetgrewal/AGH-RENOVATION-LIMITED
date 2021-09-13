from django.contrib.sitemaps import Sitemap
from blog.models import article
from myshop.urls import urlpatterns as staticUrls
from django.urls import reverse
# from django.core.urlresolvers import reverse


class PostSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9

    def items(self):
        return article.objects.all()

    def lastmod(self, obj):
        return obj.timestamp


class StaticSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    # The below method returns all urls defined in urls.py file
    def items(self):
        mylist = []
        for url in staticUrls:
            mylist.append(url.name)
        return mylist

    def location(self, item):
        return reverse(item)
