from django.contrib import admin
from .models import Product, Customer, Cart

class CartAdmin(admin.ModelAdmin):
    filter_horizontal = ('products',)

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Cart, CartAdmin)