from django.shortcuts import render

from .models import Product


def product_detail_view(request):
    obj = Product.objects.get(id=1)  # TODO: no objects objects?
    context = {'obj': obj}

    # from django.http import HttpResponse
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "product/product_detail.html", context)
