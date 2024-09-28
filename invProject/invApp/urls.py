# invApp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Public and common views
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('public/list/', views.public_product_list_view, name="public_product_list"),  # Public access
    path('search/', views.product_search_view, name="product_search"),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),

    # Authenticated product management
    path('create/', views.product_create_view, name="product_create"),
    path('list/', views.product_list_view, name="product_list"),  # Authenticated users
    path('update/<int:product_id>/', views.product_update_view, name="product_update"),
    path('delete/<int:product_id>/', views.product_delete_view, name="product_delete"),

    # Admin dashboard and management views
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin_dashboard/users/', views.user_management_view, name="user_management"), 
    path('admin_dashboard/users/create/', views.user_create_view, name='user_create'),
    path('admin_dashboard/users/update/<int:user_id>/', views.user_update_view, name='user_update'),
    path('admin_dashboard/users/delete/<int:user_id>/', views.user_delete_view, name='user_delete'),
    path('admin_dashboard/products/', views.product_management_view, name="product_management"),

    # Supplier views
    path('supplier/products/', views.supplier_products_view, name="supplier_products"),
    path('supplier/cheaper/', views.cheaper_analogues_view, name="cheaper_analogues"),

    # Buyer views
    path('buyer/products/', views.buyer_products_view, name="buyer_products"),

    path('admin_dashboard/users/', views.user_management_view, name='user_management'),
]
