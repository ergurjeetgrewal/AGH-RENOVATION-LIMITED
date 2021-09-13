from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="Home"),
    path('about', views.about,name="about"),
    path('team', views.team,name="team"),
    path('project', views.project,name="project"),
    path('contact', views.contact,name="contact"),
    path('privacy', views.privacy,name="privacy"),
    path('termsandconditions', views.termsandconditions,name="termsandconditions"),
    path('callrequest', views.callrequest,name="callrequest"),
    path('newsletters', views.newsletters,name="newsletters"),
]