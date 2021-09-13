from django.contrib import admin
from blog.models import article,Blogcomment
# Register your models here.
admin.site.register(article)
admin.site.register(Blogcomment)