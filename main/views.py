from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Testimonials
from marketing.forms import EmailSubscribeForm


def index(request):
    subscribe_form = EmailSubscribeForm()
    testimonials = Testimonials.objects.order_by('-pub_date')[:5]
    context = {
        'title': 'Home',
        'nbar': 'home',
        'testimonials': testimonials,
        'subscribe_form': subscribe_form,
    }

    return render(request, 'main/index.html', context)
