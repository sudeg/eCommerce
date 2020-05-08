from django import forms
from cart.models import Product


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': "Your name"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': "Your e-mail"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your message'
    }))


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'image',
            'description',
            'price',
            'available_colours',
            'available_sizes',
        ]
