from django.shortcuts import render
from .models import backgroundImage

# Create your views here.

def devTest2(request):

    """A view to return devTest2 page"""
    
    image = backgroundImage.objects.all()

    context = { 
        'image': image,
    }

    return render(request, 'devTest2.html', context)
