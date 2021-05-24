from django.shortcuts import render
from .models import Feature, Insights, CategoryMenu

# Create your views here.


def index(request):

    """A view to return index page"""
    feature = Feature.objects.all()
    insights = Insights.objects.all()
    category = CategoryMenu.objects.all()

    context = {
        'feature': feature,
        'insights': insights,
        'category': category,
    }

    return render(request, 'index.html', context)
