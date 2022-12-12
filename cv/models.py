import datetime
from django.utils import timezone
from django.db import models

class About(models.Model):
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=1000)
  urlimga = models.CharField(max_length=500)
  urlbg = models.CharField(max_length=500)
  urlfont = models.CharField(max_length=500)
  office = models.CharField(max_length=100)
  email = models.CharField(max_length=50)
  number = models.CharField(max_length=50)

class Project(models.Model):
  about = models.ForeignKey(About, on_delete=models.CASCADE)
  name = models.CharField(max_length=200)
  description = models.CharField(max_length=2000)
  pub_date = models.DateTimeField("Date Published")

  def __str__(self):
    return self.name
  
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Experience(models.Model):
  about = models.ForeignKey(About, on_delete=models.CASCADE)
  company= models.CharField(max_length=200)
  url= models.CharField(max_length=200)
  urlimg= models.CharField(max_length=200)

  def __str__(self):
    return self.company