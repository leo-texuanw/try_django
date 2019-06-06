from django.urls import path

from . import views

app_name = 'product'

urlpatterns = [
    path('', views.product_list_view, name='product-list'),
    path('list', views.product_list_view, name='product-list'),
    path('<int:my_id>', views.product_lookup_view, name='product-lookup'),
    path('create', views.product_create_view, name='product-create'),
    path('create_raw', views.product_create_raw_view, name='product-create-raw'),
    path('<int:id>/delete/', views.product_delete_view, name='product-delete'),
]
