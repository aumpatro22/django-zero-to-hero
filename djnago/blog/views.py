from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def go_blog(request):
    return HttpResponse("<div><p>Hello this is blog page</p></div>")
