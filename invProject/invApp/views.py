# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.models import User
from .forms import ProductForm
from .models import Product
from django import forms

# Helper function to check if a user is an admin
def is_admin(user):
    return user.is_superuser

# Landing Page - Show products to everyone, but only show admin options to logged-in users
def home_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/home.html', {'products': products})

# Public search view for products
def product_search_view(request):
    query = request.GET.get('q', None)
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()  # Show all if no query
    return render(request, 'invApp/product_search.html', {'products': products, 'query': query})

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

# Admin section: User management - List users
@user_passes_test(is_admin)
def user_management_view(request):
    users = User.objects.all()
    return render(request, 'invApp/user_management.html', {'users': users})

# Admin section: User creation
@user_passes_test(is_admin)
def user_create_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = UserCreationForm()
    return render(request, 'invApp/user_form.html', {'form': form})

# Custom form for updating user information (including admin status)
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']

# Admin section: User update (including admin status)
@user_passes_test(is_admin)
def user_update_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_management')
    else:
        form = UserUpdateForm(instance=user)
    return render(request, 'invApp/user_update_form.html', {'form': form})

# Admin section: User deletion
@user_passes_test(is_admin)
def user_delete_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_management')
    return render(request, 'invApp/user_confirm_delete.html', {'user': user})

# View for listing products (available to all users)
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_list.html', {'products': products})

# View for creating a product (requires admin access)
@user_passes_test(is_admin)
def product_create_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'invApp/product_form.html', {'form': form})

# View for updating a product (requires admin access)
@user_passes_test(is_admin)
def product_update_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'invApp/product_form.html', {'form': form})

# View for deleting a product (requires admin access)
@user_passes_test(is_admin)
def product_delete_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'invApp/product_confirm_delete.html', {'product': product})

# Detailed view for a single product (includes cheaper alternatives)
def product_detail_view(request, product_id):
    product = get_object_or_404(Product, product_id=product_id)
    cheaper_products = Product.objects.filter(sku=product.sku, price__lt=product.price).exclude(product_id=product.product_id)
    return render(request, 'invApp/product_detail.html', {
        'product': product,
        'cheaper_products': cheaper_products
    })

# View for public product listing
def public_product_list_view(request):
    products = Product.objects.all()  # Fetch all products (or apply any public filter you want)
    context = {
        'products': products,
    }
    return render(request, 'invApp/public_product_list.html', context)

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    products_count = Product.objects.count()
    users_count = User.objects.count()
    
    context = {
        'products_count': products_count,
        'users_count': users_count,
    }
    return render(request, 'invApp/admin_dashboard.html', context)

@login_required
@user_passes_test(is_admin)
def product_management_view(request):
    products = Product.objects.all()
    return render(request, 'invApp/product_management.html', {'products': products})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Suppliers').exists())
def supplier_products_view(request):
    supplier_products = Product.objects.filter(supplier=request.user)
    return render(request, 'invApp/supplier_products.html', {'products': supplier_products})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Suppliers').exists())
def cheaper_analogues_view(request):
    supplier_products = Product.objects.filter(supplier=request.user)
    analogues = []

    for product in supplier_products:
        cheaper_products = Product.objects.filter(sku=product.sku, price__lt=product.price).exclude(supplier=request.user)
        if cheaper_products.exists():
            analogues.append({'product': product, 'cheaper': cheaper_products})

    return render(request, 'invApp/cheaper_analogues.html', {'analogues': analogues})

@login_required
@user_passes_test(lambda u: u.groups.filter(name='Buyers').exists())
def buyer_products_view(request):
    products = Product.objects.filter(stock_status='in_stock')
    return render(request, 'invApp/buyer_products.html', {'products': products})
