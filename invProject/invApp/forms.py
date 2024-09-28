from django import forms
from django.contrib.auth.models import User
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id': 'Product ID',
            'name': 'Name',
            'sku': 'SKU',
            'price': 'Price',
            'quantity': 'Quantity',
            'supplier': 'Supplier'
        }

        widgets = {
            'product_id': forms.NumberInput(
                attrs={'placeholder': 'e.g 1', 'class': 'form-control'}),
            'name': forms.TextInput(
                attrs={'placeholder': 'e.g Product Name', 'class': 'form-control'}),
            'sku': forms.TextInput(
                attrs={'placeholder': 'e.g SKU123', 'class': 'form-control'}),
            'price': forms.NumberInput(
                attrs={'placeholder': 'e.g 99.99', 'class': 'form-control'}),
            'quantity': forms.NumberInput(
                attrs={'placeholder': 'e.g 10', 'class': 'form-control'}),
            'supplier': forms.TextInput(
                attrs={'placeholder': 'Supplier Name', 'class': 'form-control'})
        }

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']
        labels = {
            'username': 'Username',
            'email': 'Email',
            'is_superuser': forms.CheckboxInput(),
        }

        widgets = {
            'username': forms.TextInput(
                attrs={'placeholder': 'e.g johndoe', 'class': 'form-control'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'e.g johndoe@example.com', 'class': 'form-control'}),
            'is_superuser': forms.CheckboxInput(
                attrs={'class': 'form-check-input'}),
        }
