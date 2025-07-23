from django import forms 
from .models import Product 

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product 
        fields = [
            'name',
            'price'
        ]


class RawProductForm(forms.Form):
    name = forms.CharField(max_length=60)
    price = forms.DecimalField(max_digits=100)