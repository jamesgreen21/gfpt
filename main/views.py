from django.shortcuts import render

from .models import Testimonials


def index(request):
    testimonials = Testimonials.objects.order_by('-pub_date')[:5]
    context = {'testimonials': testimonials}
    return render(request, 'main/index.html', context)