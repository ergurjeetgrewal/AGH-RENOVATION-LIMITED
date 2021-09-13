from django.db import models

# Create your models here.
class Quotecall(models.Model):
    serial_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
class Request_Form(models.Model):
    serial_no=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=50)
    msg=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class newsletter(models.Model):
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.email

class happyclient(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    review = models.TextField()
    image = models.ImageField(upload_to="myshop/clients", default="")

    def __str__(self):
        return self.name

class projectimage(models.Model):
    s_no = models.AutoField(primary_key=True)
    ptype = models.CharField(max_length=50)
    place=models.CharField(max_length=50)  
    image = models.ImageField(upload_to="myshop/project", default="")

    def __str__(self):
        return self.ptype
    