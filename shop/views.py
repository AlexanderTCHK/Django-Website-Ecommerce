from django.shortcuts import render

def shop(request):
    context = {}
    return render(request, 'shop/shop.html', context)

def cart_list(request):
    context = {}
    return render(request, 'shop/cart_list.html', context)

def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
