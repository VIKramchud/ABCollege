from django.db import models

# Create your models here.
#class destination:
    #id : int
    #name : str
    #img : str
    #desc : str
    #price : int
    #offer : bool

class destination(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField (default = False)





class postinternship(models.Model):
    
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    salary = models.IntegerField()
    duration = models.DurationField()
    eligiblity = models.CharField(max_length=800)
    isvacant = models.BooleanField (default = False)

class scholarship(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to = 'pics')
    link = models.CharField(max_length=200)
    amount = models.IntegerField()
    eligiblity = models.CharField(max_length=400)

class events(models.Model):
    name = models.CharField(max_length=200)
    img =  models.ImageField(upload_to = 'pics')
    link =  models.CharField(max_length=200)
    time = models.DurationField()
    venue = models.CharField(max_length=200)
