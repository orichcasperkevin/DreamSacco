

from django.urls import path
from . import views

urlpatterns = [
    path(r'music/', views.index,name="index"),

]