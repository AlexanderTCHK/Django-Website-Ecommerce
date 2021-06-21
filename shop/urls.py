from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart_list/', views.cart_list, name="cart_list"),
    path('checkout/', views.checkout, name="checkout"),

]