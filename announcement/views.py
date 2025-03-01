from django.shortcuts import render
from .models import information

def get_anouncements(request):
    
    temp = information.objects.all()
    
    return render(request, "components/anouncement_cards.html", context={ "information" : temp})