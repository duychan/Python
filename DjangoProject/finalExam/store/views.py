from django.shortcuts import render

# Create your views here.

def store(req):
    context = {'name': 'store'}
    return render(req, 'store/store.html', context)

def cart(req):
    context = {"name" : 'cart'}
    return render(req, 'store/cart.html', context)

def checkout(req):
    context = {'name' : 'checkout'}
    return render(req, 'store/checkout.html', context)

def main(req):
    context = {'name' : 'error'}
    return render(req, 'store/main.html', context)