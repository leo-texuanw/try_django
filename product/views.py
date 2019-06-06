from django.http import HttpResponse
from django.shortcuts import render

from .models import Product


def product_detail_view(request):
    return HttpResponse("<h1>hello world</h1>")
