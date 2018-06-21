from django.urls import path
from . import views

app_name = 'home'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.index3, name='index3'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('pricing', views.pricing, name='pricing'),
    path('services', views.services, name='services'),



]