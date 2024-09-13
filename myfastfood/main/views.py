from django.shortcuts import render
from .models import *

def main(request):
    categories = Category.objects.prefetch_related('items').all()
    return render(request, 'index.html', {'categories': categories})

def about(request, slug=None):
    persons = Person.objects.all()
    return render(request, 'about.html', {'persons':persons})

def contact(request):
    return render(request, 'contact.html')

