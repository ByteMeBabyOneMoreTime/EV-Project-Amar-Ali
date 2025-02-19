from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def contact_us(request):
    return render(request, 'pages/contact_us.html')

def services(request):
    return render(request, 'pages/services.html')