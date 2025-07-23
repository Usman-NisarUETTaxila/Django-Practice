from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views import View 
from .models import Product
from .forms import ProductForm, RawProductForm

# Create your views here.
class ProductDetailView(View):
    def get(self, request, id):
        obj = get_object_or_404(Product, id=id)
        context = {
            'object': obj
        }
        return render(request, 'product/detail.html', context)

def product_create_view(request):
    form = RawProductForm()
    if request.method == "POST":
        form = RawProductForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
        else: 
            print(form.errors)
    context = {
        'form': form
    }
    return render(request, 'product/create.html', context)

# def product_create_view(request):
#     form = ProductForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data)
#         form.save()
#     else: 
#         print(form.errors)
#     context = {
#         'form': form
#     }
#     return render(request, 'product/create.html', context)