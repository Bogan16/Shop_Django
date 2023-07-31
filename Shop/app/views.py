from django.shortcuts import render
from app.models import Product, Customer, Cart

def homepage(request):
    # cart_detail = request.GET.get('cart_id')
    carts = Cart.objects.prefetch_related('products').all()
    customers = Customer.objects.all()
    products = Product.objects.all()
    return render(request, 'app/homepage.html', {'carts': carts, 'customers': customers, 'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)
    return render(request, 'app/product.html', {'product': product})

def customer_detail(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    return render(request, 'app/customer.html', {'customer': customer})

def cart_detail(request, cart_id):
    cart = Cart.objects.get(pk=cart_id)
    products = cart.products.all()
    return render(request, 'app/cart.html', {'cart': cart, 'products': products})