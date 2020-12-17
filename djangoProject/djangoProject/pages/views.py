from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, entity_choices, state_choices

from listings.models import Listing
from realtors.models import Entity

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'entity_choices': entity_choices,
        'price_choices': price_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # Get all realtors
    entities = Entity.objects.order_by('-book_date')

    # Get MVP(s)
    mvp_entities = Entity.objects.all().filter(is_mvp=True)

    context = {
        'entities': entities,
        'mvp_entities': mvp_entities
    }

    return render(request, 'pages/about.html', context)