from django.urls import path

from . import views

urlpatterns = [
    path('', views.product_detail_view),
    path('create', views.product_create_view),
    path('create_raw', views.product_create_raw_view),
]
