from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def music(request):
    return render(request, 'music.html')

def contact(request):
    return render(request, 'contact.html')

def portfolio(request):
    return render(request, 'portfolio.html')

# Create your views here.
