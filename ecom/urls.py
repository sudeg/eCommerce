from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', views.HomeView.as_view(), name='index'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('core/', include('core.urls', namespace='core')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('staff/', include('staff.urls', namespace='staff')),
    path('404/', views.FourOfourView.as_view(), name='404'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('about-personal/', views.AboutPersonalView.as_view(), name='about-personal'),

    path('blog-grid/', views.BlogGridView.as_view(), name='blog-grid'),
    path('blog-masonry/', views.BlogMasonryView.as_view(), name='blog-masonry'),
    path('blog-single/', views.BlogSingleView.as_view(), name='blog-single'),
    path('blog/', views.BlogView.as_view(), name='blog'),
    #     path('cart/', views.CartView.as_view(), name='cart'),
    path('contact_2/', views.Contact2View.as_view(), name='contact_2'),
    path('index2/', views.index2View.as_view(), name='index2'),
    path('index3/', views.index3View.as_view(), name='index3'),
    path('index4/', views.index4View.as_view(), name='index4'),
    path('index5/', views.index5View.as_view(), name='index5'),
    path('index6/', views.index6View.as_view(), name='index6'),
    path('onepage-carousel/', views.OnePageCarouselView.as_view(),
         name='onepage-carousel'),
    path('onepage-image/', views.OnePageImageView.as_view(), name='onepage-image'),
    path('onepage-sidebarmenu/', views.OnePageSidebarMenuView.as_view(),
         name='onepage-sidebarmenu'),
    path('onepage-slider/', views.OnePageSliderView.as_view(), name='onepage-slider'),
    path('onepage-slideshow/', views.OnePageSlideshowView.as_view(),
         name='onepage-slideshow'),
    path('onepage-video/', views.OnePageVideoView.as_view(), name='onepage-video'),
    path('onepage-single/', views.OnePageSingleView.as_view(), name='onepage-single'),
    path('portfolio-single/', views.PortfolioSingleView.as_view(),
         name='portfolio-single'),
    path('portfolio-single2/', views.PortfolioSingle2View.as_view(),
         name='portfolio-single2'),
    path('portfolio-single3/', views.PortfolioSingle3View.as_view(),
         name='portfolio-single3'),
    path('portfolio-single4/', views.PortfolioSingle4View.as_view(),
         name='portfolio-single4'),
    path('portfolio-single5/', views.PortfolioSingle5View.as_view(),
         name='portfolio-single5'),
    path('portfolio-single6/', views.PortfolioSingle6View.as_view(),
         name='portfolio-single6'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    path('portfolio2/', views.Portfolio2View.as_view(), name='portfolio2'),
    path('portfolio3/', views.Portfolio3View.as_view(), name='portfolio3'),
    path('portfolio4/', views.Portfolio4View.as_view(), name='portfolio4'),
    path('portfolio5/', views.Portfolio5View.as_view(), name='portfolio5'),
    path('portfolio6/', views.Portfolio6View.as_view(), name='portfolio6'),
    path('portfolio7/', views.Portfolio7View.as_view(), name='portfolio7'),
    path('portfolio8/', views.Portfolio8View.as_view(), name='portfolio8'),
    path('portfolio9/', views.Portfolio9View.as_view(), name='portfolio9'),
    #     path('product-single/', views.ProductSingleView.as_view(), name='product-single'),
    path('services/', views.ServicesView.as_view(), name='services'),
    path('scripts/', views.ScriptsView.as_view(), name='scripts'),




]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
