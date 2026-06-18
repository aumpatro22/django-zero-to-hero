from django.urls import path 
from .views import home_view,product_views

urlpatterns = [
    path('',home_view,name='home'),
    path('products/',product_views,name='product'),
]