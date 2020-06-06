from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('personalDimensionalPrinters/', views.PersonalDimensionalPrinterListView.as_view(),name='personalDimensionalPrinters-list'),
    path('personalDimensionalPrinters/<pk>/delete/',views.PersonalDimensionalPrinterDeleteView.as_view(), name='dimensionalPrinters-delete'),
    path('settings/', views.PersonalInfoUpdateView.as_view(),name='personalInfo-update'),
]
