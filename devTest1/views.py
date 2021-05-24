from django.shortcuts import render
from .models import Feature, Insights

# Create your views here.


def index(request):

    """A view to return index page"""
    feature = Feature.objects.all()
    insights = Insights.objects.all()

    context = {
        'feature': feature,
        'insights': insights,
    }

    return render(request, 'index.html', context)
