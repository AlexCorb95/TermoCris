from django import forms
from django.forms import TextInput

from products.models import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['product_name', 'product_short_desc', 'product_description', 'product_price', 'product_img']

        widgets = {
            'product_name': TextInput(attrs={'placeholder': 'Numele produsului', 'class': 'form-control'}),
            'product_short_desc': TextInput(attrs={'placeholder': 'Scurta descriere', 'class': 'form-control'}),
            'product_description': TextInput(attrs={'placeholder': 'Descrierea produsului', 'class': 'form-control'}),
            'product_price': TextInput(attrs={'placeholder': 'Pret produs', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product_img'].widget.attrs['class'] = 'form-control'
