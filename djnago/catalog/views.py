from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Welcome to the Product Catalog Engine Room!</h1>")
    
def product_views(request):
    catalog_title = "Engine of latest phone"
    product_list = ["oppo find x", "OnePlus-13", "iphone 7"]
    in_stock = True
    context = {
        'title': catalog_title,
        'products': product_list,
        'is_available': in_stock, 
    }
    return render(request, 'catalog/product.html', context)