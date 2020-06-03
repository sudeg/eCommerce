from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import reverse, render, redirect
from django.views import generic
from cart.models import Order, Product
from core.models import *
from .forms import *
from django.http import HttpResponse


class ProfileView(generic.TemplateView):
    template_name = 'profile.html'


class FirstPage(generic.TemplateView):
    template_name = 'index_hex.html'


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class FourOfourView(generic.TemplateView):
    template_name = '404.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ProductSingleView(generic.TemplateView):
    template_name = 'product_detail.html'


class ScriptsView(generic.TemplateView):
    template_name = 'scripts.html'


class ServicesView(generic.TemplateView):
    template_name = 'services.html'


# class ShopView(generic.TemplateView):
#     template_name = 'shop.html'


class CartView(generic.TemplateView):
    template_name = 'cart.html'


class ContactView(generic.FormView):
    form_class = ContactForm
    template_name = 'contact.html'

    def get_success_url(self):
        return reverse("contact")

    def form_valid(self, form):
        messages.info(
            self.request, "Thanks for getting in touch. We have received your message.")
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')

        full_message = f"""
            Received message below from {name}, {email}
            ________________________


            {message}
            """
        send_mail(
            subject="Received contact form submission",
            message=full_message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.NOTIFY_EMAIL]
        )
        return super(ContactView, self).form_valid(form)
