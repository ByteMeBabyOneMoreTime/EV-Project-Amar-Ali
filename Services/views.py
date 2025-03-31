from Services.models import Service
from django.shortcuts import render


def load_services(request):
    # Get all services with their related perks
    services = Service.objects.prefetch_related('perks_set').all()
    context = {
        'services': services
    }
    return render(request, 'components/service_cards.html', context)

