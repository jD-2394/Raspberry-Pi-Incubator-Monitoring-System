from django.db import models
from django.forms import ModelForm
from .choices import *

class EggInfo(models.Model):

    breed = models.CharField(max_length=100,default="Some Chicken")
    typeOfEgg = models.CharField(max_length=100,choices=EGG_TYPE,default="Chicken")
    sizeOfEgg = models.CharField(max_length=100,choices=EGG_SIZE,default="Small")


