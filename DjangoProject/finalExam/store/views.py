from django.shortcuts import render
from .models import *
import datetime
# Create your views here.

def store(req):
    products = Product.objects.all()
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
        countItem = order['getTotalItem']
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
        countItem = order['getTotalItem']
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
        countItem = order['getTotalItem']
    context = {
        "items" : items,
        "order" : order,
        "countItem" : countItem
        }
    return render(req, 'store/checkout.html', context)

def main(req):
    context = {
        }
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
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        order.transactionId = transactionId
        
        ShippingAddress.objects.create(customer= customer,
        order= order, address= shippingInfo['address'], city= shippingInfo['city'],
        phoneNumber= shippingInfo['phone_number'])
        print(userInfo['total'],order.getTotalBill )
        if userInfo['total'] == order.getTotalBill:
            order.complete = True
        order.save()
    return JsonResponse("Payment completed", safe= False)