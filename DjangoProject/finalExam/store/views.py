from django.shortcuts import render
from .models import *
# Create your views here.

def store(req):
    products = Product.objects.all()
    context = {'products': products}
    return render(req, 'store/store.html', context)

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()

    else:
        items = []

    context = {
        "items" : items,
        "order" : order,
        }

    return render(req, 'store/cart.html', context)

def checkout(req):
    context = {'name' : 'checkout'}
    return render(req, 'store/checkout.html', context)

def main(req):
    context = {'name' : 'error'}
    return render(req, 'store/main.html', context)