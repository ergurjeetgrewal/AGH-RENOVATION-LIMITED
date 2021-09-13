from django.urls import path,include
from . import views
from django.contrib.sitemaps.views import sitemap
from django.conf.urls import url
from blog.sitemaps import PostSitemap, StaticSitemap

sitemaps = {
    'posts': PostSitemap,
    'static': StaticSitemap()
}

urlpatterns = [
    path('', views.index,name="Home"),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    # path('articles/<int:artid>', views.articles,name="articles"),
    path('usercomment', views.usercomment,name="usercomment"),
    path('<str:slug>', views.articles,name="articles"),
]