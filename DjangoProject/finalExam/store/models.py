from django.db import models
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.name
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transactionId = models.CharField(max_length=200, null=True)
    def __str_(self):
        return str(self.id)
    
    @property
    def getTotalBill(self):
        orderItems = self.orderitem_set.all()
        total = sum([i.totalBill for i in orderItems])
        return "{:,.0f}".format(total)
    
    @property
    def getTotalItem(self):
        orderItems = self.orderitem_set.all()
        return sum([i.quantity for i in orderItems])

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null= True, blank= True)
    def __str__(self):
        return self.name
    
    @property
    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    @property
    def formatCur(self):
        amount = self.price
        currency = "{:,.0f}".format(amount)
        return currency

class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank= True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank= True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    dateAdded = models.DateTimeField(auto_now_add=True)
    
    @property
    def totalBill(self):
        return self.product.price * self.quantity
    
    @property
    def formatCur(self):
        amount = self.totalBill
        currency = "{:,.0f}".format(amount)
        return currency
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    phoneNumber = models.CharField(null=True,max_length=11)
    dateAdded = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address


