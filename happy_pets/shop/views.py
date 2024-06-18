from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Product, Order, OrderItem,Cart,CartItem, Review
from .forms import ReviewForm, ProductForm, CartItemForm

def home(request):
    return render(request, 'shop/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = CartItemForm(request.POST)
        if form.is_valid():
            cart_item = form.save(commit=False)
            cart_item.cart = cart
            cart_item.save()
            return redirect('view_cart')
    else:
        form = CartItemForm(initial={'product': product})
    return render(request, 'shop/add_to_cart.html', {'form': form, 'product': product})

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'shop/view_cart.html', {'cart_items': cart_items})

@login_required
def place_order(request):
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                OrderItem.objects.create(order=order, product=item.product, quantity=item.quantity)
            cart_items.delete()
            return redirect('order_history')
    else:
        form = OrderForm()
    return render(request, 'shop/place_order.html', {'form': form})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'shop/order_history.html', {'orders': orders})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})


def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect('product_detail', pk=product.id)
    else:
        form = ReviewForm()
    return render(request, 'shop/add_review.html', {'form': form, 'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    
    
    order, created = Order.objects.get_or_create(user=request.user, is_ordered=False)
    
    
    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)
    
    
    order_item.quantity += 1
    order_item.save()

    messages.success(request, f"{product.name} added to cart successfully.")
    return redirect('product_detail', pk=product.id)

@login_required
def cart(request):
    order = Order.objects.filter(user=request.user, is_ordered=False).first()
    items = order.items.all() if order else []
    return render(request, 'shop/cart.html', {'order': order, 'items': items})

def home(request):
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all()
    return render(request, 'shop/product_detail.html', {'product': product, 'reviews': reviews})

@login_required
def checkout(request):
    order = Order.objects.get(user=request.user, is_ordered=False)
    if request.method == 'POST':
        
        order.is_ordered = True
        order.save()
        return redirect('order_confirmation', pk=order.pk)
    return render(request, 'shop/checkout.html', {'order': order})

@login_required
def order_confirmation(request, pk):
    order = get_object_or_404(Order, pk=pk, user=request.user)
    return render(request, 'shop/order_confirmation.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user, is_ordered=True)
    return render(request, 'shop/order_history.html', {'orders': orders})

@staff_member_required
def custom_admin_home(request):
    return render(request, 'shop/admin_home.html')

@staff_member_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('custom_admin_home')
    else:
        form = ProductForm()
    return render(request, 'shop/add_product.html', {'form': form})

@staff_member_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('custom_admin_home')
    else:
        form = ProductForm(instance=product)
    return render(request, 'shop/update_product.html', {'form': form})

@staff_member_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('custom_admin_home')
    return render(request, 'shop/delete_product.html', {'product': product})
