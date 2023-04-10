from django.db import models

# Create your models here.
class Clients(models.Model):
    c_name = models.CharField(max_length=50)
    c_email = models.EmailField( max_length=254)
    c_message = models.TextField( max_length=750)
# we will use it if we want to see details of row by their name 
    # def __str__(self):
    #      return self.c_name
