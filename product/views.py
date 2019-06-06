from django.shortcuts import render

from .models import Product
from .forms import ProductForm, RawProductForm


def product_detail_view(request):
    obj = Product.objects.get(id=1)

    context = {
        'obj': obj
    }

    # from django.http import HttpResponse
    # return HttpResponse("<h1>hello world</h1>")
    return render(request, "product/product_detail.html", context)


def product_create_view(request):
    """ A better way of impl `product_create_raw_view`  """
    # title = request.POST.get('title')     # get one specific field

    initial_data = {
        'title': "my awesome title",
    }

    # add new record to db
    form = ProductForm(request.POST or None, initial=initial_data)

    # mod record in db
    # obj = Product.objects.get(id=1)
    # form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm()    # reset after submit

    context = {
        'form': form
    }

    return render(request, "product/product_create.html", context)


def product_create_raw_view(request):
    my_form = RawProductForm()      # try with and without request.GET as a param
    if request.method == 'POST':
        my_form = RawProductForm(request.POST)

        if my_form.is_valid():
            Product.objects.create(**my_form.cleaned_data)
            my_form = RawProductForm()
        else:
            print(my_form.errors)

    context = {
        'form': my_form
    }

    return render(request, "product/product_create.html", context)
