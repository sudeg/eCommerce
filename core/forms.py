from django import forms
from cart.models import *
from core.models import *


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


class DesignerForm(forms.ModelForm):
    class Meta:
        model = Designer
        fields = [
            'brand',
            'image',
            'description',
            'email',
            'countDesignerPros',

        ]


class PrinterOwnerForm(forms.ModelForm):
    class Meta:
        model = PrinterOwner
        fields = [
            'brand',
            'image',
            'description',

        ]


class DimensionalPrinterForm(forms.ModelForm):
    class Meta:
        model = DimensionalPrinter
        fields = [
            'title',
            'brand',
            'image',
            'description',
            'price',
            'email',


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
