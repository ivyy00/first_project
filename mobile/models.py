from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    icon=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name
       
class Cosutmer(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=250)
    phone=models.CharField(max_length=20)
    email=models.CharField( max_length=50)

class Products(models.Model):
    name=models.CharField(max_length=100)
    brand=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=6)
    storge=models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    image=models.ImageField(upload_to='mobile/static/images', null=True )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Cart(models.Model):
      user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
      session_id=models.CharField( max_length=100,null=True,blank=True)
      product=models.ForeignKey(Products,on_delete=models.CASCADE)
      quntity=models.PositiveBigIntegerField(default=1)
      created_at=models.DateTimeField(auto_now_add=True)

      def get_total_price(self):
        return self.quntity * self.product.price
      
      def get_cart_items(self):
        return Cart.objects.filter(user=self.user)
      
      def get_cart_total(self):
        return sum(item.get_total_price() for item in self.get_cart_items())


