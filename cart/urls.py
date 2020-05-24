from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='summary'),
    path('shop/', views.DesignTypesView.as_view(), name='designType-list'),
    path('shop/designs/', views.ProductListView.as_view(), name='product-list'),
    path('shop/<slug>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('increase-quantity/<pk>/',
         views.IncreaseQuantityView.as_view(), name='increase-quantity'),
    path('decrease-quantity/<pk>/',
         views.DecreaseQuantityView.as_view(), name='decrease-quantity'),
    path('remove-from-cart/<pk>/',
         views.RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('thank-you/', views.ThankYouView.as_view(), name='thank-you'),
    path('confirm-order/', views.ConfirmOrderView.as_view(), name='confirm-order'),
    path('printerFinder/', views.PrinterFinderView.as_view(), name='printer-finder'),
    path('shop/designs/toys/',
         views.ToysListView.as_view(), name='toys-list'),
    path('shop/designs/gardening/',
         views.GardeningListView.as_view(), name='gardening-list'),
    path('shop/designs/scraps/',
         views.ScrapsListView.as_view(), name='scraps-list'),
    path('shop/designs/shapes/',
         views.ShapesListView.as_view(), name='shapes-list'),
    path('shop/designs/architecture/',
         views.ArchitectureListView.as_view(), name='architecture-list'),
    path('shop/designs/essentials/',
         views.EssentialsListView.as_view(), name='essentials-list'),
    path('shop/designs/robotic/',
         views.RoboticListView.as_view(), name='robotic-list'),
    path('shop/designs/accessories/',
         views.AccessoriesListView.as_view(), name='accessories-list'),
    path('shop/designs/kitchen/',
         views.KitchenListView.as_view(), name='kitchen-list'),
    path('shop/designs/all/',
         views.DesignsView.as_view(), name='designs-list'),


]
