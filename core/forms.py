from django import forms
from cart.models import Product
from core.models import *


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': "Your name"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': "Your e-mail"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Your message'}))


class ProductForm(forms.ModelForm):
    class Meta:
        fields = [
            'title',
            'image',
            'description',
            'price',
            'available_colours',
            'available_sizes',
        ]

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        fields = [
            'age',
            'image',
            'info',
            'fullName',
            'email',
        ]


class PrinterForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = [
            'brand',
            'modelName',
            'imageOne',
            'imageTwo',
            'imageThree',

        ]
