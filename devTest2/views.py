from django.shortcuts import render
from .models import backgroundImage, breadcrumbs, frames, headline

# Create your views here.

def devTest2(request):

    """A view to return devTest2 page"""
    
    image = backgroundImage.objects.all()
    breadcrumb = breadcrumbs.objects.all()
    frame = frames.objects.all()
    head = headline.objects.all()

    context = { 
        'image': image,
        'breadcrumb': breadcrumb,
        'frame': frame,
        'head': head,
    }

    return render(request, 'devTest2.html', context)
