# invApp/urls.py
from django.urls import path
from . import views

# invApp/urls.py
urlpatterns = [
    path('', views.home_view, name="home"),
    path('login/', views.login_view, name="login_view"),
    path('logout/', views.logout_view, name="logout_view"),
    path('create/', views.product_create_view, name="product_create"),
    path('list/', views.product_list_view, name="product_list"),  # Authenticated users
    path('public/list/', views.public_product_list_view, name="public_product_list"),  # Public access
    path('update/<int:product_id>/', views.product_update_view, name="product_update"),
    path('delete/<int:product_id>/', views.product_delete_view, name="product_delete"),
    path('admin_dashboard/', views.admin_dashboard, name="admin_dashboard"),
    path('admin/users/', views.user_management_view, name="user_management"),
    path('admin/products/', views.product_management_view, name="product_management"),
    path('supplier/products/', views.supplier_products_view, name="supplier_products"),
    path('supplier/cheaper/', views.cheaper_analogues_view, name="cheaper_analogues"),
    path('buyer/products/', views.buyer_products_view, name="buyer_products"),
    path('search/', views.product_search_view, name="product_search"),
    path('product/<int:product_id>/', views.product_detail_view, name='product_detail'),
]

