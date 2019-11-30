from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Product
from .forms import ProductForm, RawProductForm


def product_lookup_view(request, my_id=1):
    # my_id is defined in urls.py
    # Method 1:
    obj = get_object_or_404(Product, id=my_id)

    # Method 2:
    # try:
    #     obj = Product.objects.get(id=my_id)
    # except Product.DoesNotExist:
    #     raise Http404

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


def product_update_view(request, id):
    # mod record in db
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        form = ProductForm()    # reset after submit

    context = {
        'form': form
    }

    return render(request, "product/product_create.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)

    # POST request
    if request.method == 'POST':
        # confirming delete
        obj.delete()
        return redirect('../../')

    context = {
            "object": obj
    }
    return render(request, "product/product_delete.html", context)

def product_list_view(request):
    queryset = Product.objects.all()
    context = {
            "object_list": queryset,
    }
    return render(request, "product/product_list.html", context)
