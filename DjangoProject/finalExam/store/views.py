from functools import total_ordering
from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def store(req):
    products = Product.objects.all()
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        countItem = order.getTotalItem
    else:
        order = {"getTotalBill": 0,
                 "getTotalItem": 0
                 }
        countItem = 0
        try:
            cart = json.loads(req.COOKIES['cart'])
        except:
            cart = {}
        for i in cart:
            countItem += cart[i]["quantity"]
    context = {'products': products,"countItem": countItem}
    return render(req, 'store/store.html', context)

def cart(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        countItem = order.getTotalItem
    else:
        items = []
        order = {"getTotalBill": 0,
                 "getTotalItem": 0
                 }
        countItem = 0
        total = 0
        try:
            cart = json.loads(req.COOKIES['cart'])
        except:
            cart = {}
        for i in cart:
            countItem += cart[i]["quantity"]
            product = Product.objects.get(id=i)
            total += cart[i]['quantity'] * product.price
            order['getTotalBill'] = total
            order['getTotalItem'] = countItem
            item = {
                'product': product,
                'quantity': cart[i]['quantity'],
                'formatCur': cart[i]['quantity'] * product.price
            }
            items.append(item)
    context = {
        "items" : items,
        "order" : order,
        "countItem": countItem 
        }
    return render(req, 'store/cart.html', context)

def checkout(req):
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        countItem = order.getTotalItem
    else:
        items = []
        order = {"getTotalBill": 0,
                 "getTotalItem": 0
                 }
        countItem = 0
        totalItems = 0
        try:
            cart = json.loads(req.COOKIES['cart'])
        except:
            cart = {}
        for i in cart:
            countItem += cart[i]["quantity"]
            quantity = cart[i]['quantity']
            totalItems += quantity
            product = Product.objects.get(id=i)
            order['getTotalBill'] = product.price * totalItems
            order['getTotalItem'] = totalItems
            totalBill = product.price * quantity
            item = {
                'product': product,
                'quantity': quantity,
                'totalBill': totalBill,
            }
            items.append(item)
    context = {
        "items" : items,
        "order" : order,
        "countItem": countItem
        }
    return render(req, 'store/checkout.html', context)

def main(req):
    context = {}
    return render(req, 'store/main.html', context)

def updateItem(req):
    response = json.loads(req.body)
    productId = response['productId']
    action = response['action']
    customer = req.user.customer
    product = Product.objects.get(id= productId)
    order, created = Order.objects.get_or_create(customer= customer, complete= False)
    orderItem, created = OrderItem.objects.get_or_create(order= order, product= product)
    if action == 'add':
        orderItem.quantity += 1
    if action == 'remove':
            orderItem.quantity -= 1
    orderItem.save()
    if orderItem.quantity <= 0:
            try:
                orderItem.delete()
            except:
                print("not deleted yet")
    return JsonResponse("Item was added", safe= False)

def processOrder(req):
    response = json.loads(req.body)
    userInfo = response['userInfo']
    shippingInfo = response['shippingInfo']
    transactionId = datetime.datetime.now().timestamp()
    if req.user.is_authenticated:
        customer = req.user.customer
        order, created = Order.objects.get_or_create(customer = customer,
                                                     complete = False)
    else:
        name = userInfo['name']
        email = userInfo['email']
        print(name, email)
        customer = Customer.objects.create(email= email)
        customer.save()
        try:
            cart = json.loads(req.COOKIES['cart'])
        except:
            cart = {}
        for i in cart:
            quantity = cart[i]['quantity']
            product = Product.objects.get(id=i)
            order,created = Order.objects.get_or_create(customer = customer, complete = False)
            
    order.transactionId = transactionId
    orderItem = OrderItem.objects.create(order = order, product = product, quantity = quantity)
    ShippingAddress.objects.create(customer= customer,
        order= order, address= shippingInfo['address'],
        city= shippingInfo['city'],
        phoneNumber= shippingInfo['phone_number'])
    if userInfo['total'] == order.getTotalBill:
        order.complete = True
    order.save()
    return JsonResponse("Payment completed", safe= False)