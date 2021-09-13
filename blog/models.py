from django.db import models
from django.utils.timezone import now

# Create your models here.


class article(models.Model):
    s_no = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=50)
    headimage = models.ImageField(upload_to="blog/articles/featureimages", default="")
    headtitle = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    para1 = models.TextField()
    para2 = models.TextField()
    heading2 = models.CharField(max_length=50)
    para3 = models.TextField()
    featureimage = models.ImageField(upload_to="blog/articles/featureimages", default="")
    imagep1 = models.ImageField(upload_to="blog/articles/projectimages", default="")
    imagep2 = models.ImageField(upload_to="blog/articles/projectimages", default="")
    imagep3 = models.ImageField(upload_to="blog/articles/projectimages", default="")
    imagep4 = models.ImageField(upload_to="blog/articles/projectimages", default="", blank=True)
    imagep5 = models.ImageField(upload_to="blog/articles/projectimages", default="", blank=True)
    imagep6 = models.ImageField(upload_to="blog/articles/projectimages", default="", blank=True)
    timestamp = models.DateTimeField(default=now)
    

    def __str__(self):
        return self.title
    def __unicode__(self):
        return self.slug
    def get_absolute_url(self):
        return '/blog/'+self.slug

class Blogcomment(models.Model):
    sno=models.AutoField(primary_key=True)
    comment = models.TextField()
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    post = models.ForeignKey(article,on_delete=models.CASCADE)
    parent = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:15]+'... By: '+str(self.name)