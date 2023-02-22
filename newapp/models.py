from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class regmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class sregmodel(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    address=models.CharField(max_length=50)
    pincode=models.IntegerField()
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class imgmodel(models.Model):
    shopid=models.IntegerField()
    imgname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=60)
    imgfile=models.ImageField(upload_to='newapp/static')
    def __str__(self):
        return self.imgname

class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user

class cart(models.Model):
    imgname=models.CharField(max_length=400)
    prize=models.IntegerField()
    description=models.CharField(max_length=600)
    imgfile=models.ImageField()
    def __str__(self):
        return self.imgname

class wishlist(models.Model):
    imgname=models.CharField(max_length=400)
    price = models.IntegerField()
    description = models.CharField(max_length=600)
    imgfile = models.ImageField()
    def __str__(self):
        return self.imgname

class buy(models.Model):
    imgname=models.CharField(max_length=400)
    price = models.IntegerField()
    description = models.CharField(max_length=600)
    quantity=models.IntegerField()
    def __str__(self):
        return self.imgname

class customercard(models.Model):
    cardname=models.CharField(max_length=30)
    cardnumber=models.CharField(max_length=30)
    cardexpiry=models.CharField(max_length=30)
    securitycode=models.CharField(max_length=30)
    def __str__(self):
        return self.cardname