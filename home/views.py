from django.shortcuts import HttpResponse, render


def home(request):
    return render(request, "pages/index.html")

def about(request):
    return render(request, "pages/about.html")

def contact_us(request):
    return render(request, "pages/contact_us.html")

def services(request):
    return render(request, 'pages/services.html')

def announcements(request):
    return render(request, 'pages/announcements.html')

def referral_program(request):
    return render(request, 'pages/referral.html')

def join_page(request):
    return render(request, 'pages/join.html')
