from django.contrib import admin
from .models import Product, Order, OrderItem,Cart,CartItem, Review

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Review)
admin.site.register(Cart)
admin.site.register(CartItem)
