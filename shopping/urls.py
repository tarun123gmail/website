from . import views
from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index-shoppin'),
    path('home/', views.home, name='index-home'),
    path('about/', views.about, name='about-shoppin'),
    path('contact/', views.contact, name='contact-shoppin'),
    path('search/', views.search, name='search-shoppin'),
    path('productview/', views.productView, name='productview-shoppin'),
    path('tracking/', views.tracking, name='Tracking-shoppin'),
    path('checkout/', views.checkout, name='checkout-shoppin'),

]