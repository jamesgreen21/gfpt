from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login
from django.contrib import messages

from .models import Testimonials


def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You logged in")
            return redirect('index')
        else:
            messages.error(request, "You entered an incorrect username or password!")
            return redirect('accounts:login')
    else:
        form = AuthenticationForm()

    testimonials = Testimonials.objects.order_by('-pub_date')[:5]
    context = {
        'title': 'Home',
        'nbar': 'home',
        'testimonials': testimonials,
        'form': form,
    }

    return render(request, 'main/index.html', context)
