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


# class BecomeDesignerView(LoginRequiredMixin, generic.TemplateView):
class PersonalDimensionalPrinterListView(LoginRequiredMixin, generic.ListView):
    template_name = 'core/personalDimensionalPrinters.html'
    queryset = DimensionalPrinter.objects.all()
    paginate_by = 20
    context_object_name = 'dimensionalPrinters'


class PersonalDimensionalPrinterDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'core/dimensionalPrinters_delete.html'
    queryset = DimensionalPrinter.objects.all()

    def get_success_url(self):
        return reverse("core:personalDimensionalPrinters-list")


class FirstPage(generic.TemplateView):
    template_name = 'index_hex.html'


class HomeView(generic.TemplateView):
    template_name = 'index.html'


class FourOfourView(generic.TemplateView):
    template_name = '404.html'


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class AboutPersonalView(generic.TemplateView):
    template_name = 'about-personal.html'


class BlogGridView(generic.TemplateView):
    template_name = 'blog-grid.html'


class BlogMasonryView(generic.TemplateView):
    template_name = 'blog-masonry.html'


class BlogSingleView(generic.TemplateView):
    template_name = 'blog-single.html'


class BlogView(generic.TemplateView):
    template_name = 'blog.html'


class CartView(generic.TemplateView):
    template_name = 'cart.html'


class Contact2View(generic.TemplateView):
    template_name = 'contact_2.html'


class index2View(generic.TemplateView):
    template_name = 'index2.html'


class index3View(generic.TemplateView):
    template_name = 'index3.html'


class index4View(generic.TemplateView):
    template_name = 'index4.html'


class index5View(generic.TemplateView):
    template_name = 'index5.html'


class index6View(generic.TemplateView):
    template_name = 'index6.html'


class OnePageCarouselView(generic.TemplateView):
    template_name = 'onepage-carousel.html'


class OnePageImageView(generic.TemplateView):
    template_name = 'onepage-image.html'


class OnePageSidebarMenuView(generic.TemplateView):
    template_name = 'onepage-sidebarmenu.html'


class OnePageSliderView(generic.TemplateView):
    template_name = 'onepage-sliderl.html'


class OnePageSlideshowView(generic.TemplateView):
    template_name = 'onepage-slideshow.html'


class OnePageVideoView(generic.TemplateView):
    template_name = 'onepage-video.html'


class OnePageSingleView(generic.TemplateView):
    template_name = 'onepage-single.html'


class PortfolioSingleView(generic.TemplateView):
    template_name = 'portfolio-single.html'


class PortfolioSingle2View(generic.TemplateView):
    template_name = 'portfolio-single2.html'


class PortfolioSingle3View(generic.TemplateView):
    template_name = 'portfolio-single3.html'


class PortfolioSingle4View(generic.TemplateView):
    template_name = 'portfolio-single4.html'


class PortfolioSingle5View(generic.TemplateView):
    template_name = 'portfolio-single5.html'


class PortfolioSingle6View(generic.TemplateView):
    template_name = 'portfolio-single6.html'


class PortfolioView(generic.TemplateView):
    template_name = 'portfolio.html'


class Portfolio2View(generic.TemplateView):
    template_name = 'portfolio2.html'


class Portfolio3View(generic.TemplateView):
    template_name = 'portfolio3.html'


class Portfolio4View(generic.TemplateView):
    template_name = 'portfolio4.html'


class Portfolio5View(generic.TemplateView):
    template_name = 'portfolio5.html'


class Portfolio6View(generic.TemplateView):
    template_name = 'portfolio6.html'


class Portfolio7View(generic.TemplateView):
    template_name = 'portfolio7.html'


class Portfolio8View(generic.TemplateView):
    template_name = 'portfolio8.html'


class Portfolio9View(generic.TemplateView):
    template_name = 'portfolio9.html'


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


class CaravanListView(LoginRequiredMixin, generic.ListView):
    template_name = 'core/caravan_list.html'
    queryset = Product.objects.all()
    paginate_by = 20
    context_object_name = 'products'


class CaravanCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/caravan_create.html'
    form_class = ProductForm

    def get_success_url(self):
        return reverse("core:caravan-list")

    def form_valid(self, form):
        form.save()
        return super(CaravanCreateView, self).form_valid(form)


class CaravanUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'core/caravan_create.html'
    form_class = ProductForm
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("core:caravan-list")

    def form_valid(self, form):
        form.save()
        return super(CaravanUpdateView, self).form_valid(form)


class CaravanDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'core/caravan_delete.html'
    queryset = Product.objects.all()

    def get_success_url(self):
        return reverse("core:caravan-list")


class PersonalInfoUpdateView(LoginRequiredMixin, generic.CreateView):
    template_name = 'core/personalInfo_update.html'
    form_class = PersonalInfoForm

    def get_success_url(self):
        return reverse("core:profile")

    def form_valid(self, form):
        form.save()
        return super(PersonalInfoUpdateView, self).form_valid(form)


class DimensionalPrinterListView(generic.ListView):
    template_name = 'shop.html'
    queryset = DimensionalPrinter.objects.all()
