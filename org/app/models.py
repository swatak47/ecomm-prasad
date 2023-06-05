from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class contact_table(models.Model):

    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    subject =models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name



class farmer_table(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    
   
    is_farmer_table = models.BooleanField(default=True)
    is_customer_table = models.BooleanField(default=False)
    
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    username =models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=30)
    password = models.CharField(max_length=30)



    def __str__(self):
        return self.name 

class customertable(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    is_farmer_table = models.BooleanField(default=False)
    is_customertable = models.BooleanField(default=True)
    
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    username=models.CharField(max_length=100)
    
    gender=models.CharField(max_length=10)
    mobile_no=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name 
    
    