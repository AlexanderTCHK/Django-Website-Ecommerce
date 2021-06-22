from django.urls import path

from . import views

urlpatterns = [
    path('', views.shop, name="shop"),
    path('cart_list/', views.cart_list, name="cart_list"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

]