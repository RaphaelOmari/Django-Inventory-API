from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import ProductForm
from .models import Product
from django.contrib.auth.models import User

# Helper function to check if a user is an admin
def is_admin(user):
    return user.is_superuser

# Landing Page - redirect unauthorized users to login
def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'invApp/home.html')
    else:
        return redirect('login_view')

# Login functionality
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'invApp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'invApp/login.html')

# Logout functionality
def logout_view(request):
    logout(request)
    return redirect('login_view')

# Admin section: Admin dashboard
@user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'invApp/admin_dashboard.html')

# Admin section: User management
@login_required
@user_passes_test(is_admin)
def user_management_view(request):
    users = User.objects.all()
    return render(request, 'invApp/user_management.html', {'users': users})

# Admin section: Product management
@login_required
@user_passes_test(is_admin)
def product_management_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_management.html', {'products': products})

# Supplier section: List products
@login_required
def supplier_products_view(request):
    if not request.user.groups.filter(name='Suppliers').exists():
        return redirect('home')

    supplier_products = Product.objects.filter(supplier=request.user)
    return render(request, 'invApp/supplier_products.html', {'products': supplier_products})

# Supplier section: Find cheaper analogues
@login_required
def cheaper_analogues_view(request):
    if not request.user.groups.filter(name='Suppliers').exists():
        return redirect('home')

    supplier_products = Product.objects.filter(supplier=request.user)
    analogues = []

    for product in supplier_products:
        cheaper_products = Product.objects.filter(sku=product.sku, price__lt=product.price).exclude(supplier=request.user)
        if cheaper_products.exists():
            analogues.append({'product': product, 'cheaper': cheaper_products})

    return render(request, 'invApp/cheaper_analogues.html', {'analogues': analogues})

# Buyer section: View all products in stock
@login_required
def buyer_products_view(request):
    if not request.user.groups.filter(name='Buyers').exists():
        return redirect('home')

    products = Product.objects.filter(stock_status='in_stock')
    return render(request, 'invApp/buyer_products.html', {'products': products})

# View for creating a product
@login_required
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'invApp/product_form.html', {'form': form})

# View for updating a product
@login_required
def product_update_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'invApp/product_form.html', {'form': form})

# View for deleting a product
@login_required
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})
