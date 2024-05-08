from django.db import models

# Create your models here.
class ContactPage(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField(max_length=100)
    phone= models.CharField(max_length=14)
    company= models.CharField(max_length=50)
    company_website= models.CharField(max_length=50)
    services= models.CharField(max_length=50)
    describe= models.TextField(max_length=500)
    term= models.BooleanField(default=False)
    

