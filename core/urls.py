from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('create/', views.CaravanCreateView.as_view(), name='caravan-create'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('caravans/', views.CaravanListView.as_view(), name='caravan-list'),
    path('caravans/<pk>/update/',views.CaravanUpdateView.as_view(), name='caravan-update'),
    path('caravans/<pk>/delete/',views.CaravanDeleteView.as_view(), name='caravan-delete'),
    path('personalDimensionalPrinters/', views.PersonalDimensionalPrinterListView.as_view(),name='personalDimensionalPrinters-list'),
    path('personalDimensionalPrinters/<pk>/delete/',views.PersonalDimensionalPrinterDeleteView.as_view(), name='dimensionalPrinters-delete'),
    path('settings/', views.PersonalInfoUpdateView.as_view(),name='personalInfo-update'),
]
