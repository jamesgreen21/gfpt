from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import (
    UserRegisterForm,
    UserUpdateForm,
    ProfileRegisterForm,
)


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, "You are logged out")
    return redirect('index')


def register(request):
    """
    Returns a view that renders the register page and form
    """
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.. Lets do this!')
            return redirect('index')
    else:
        form = UserRegisterForm()

    context = {
        'title': 'Accounts',
        'nbar': 'accounts',
        'form': form,
    }
    return render(request, 'register.html', context)


@login_required
def profile(request):
    """
    Returns a view that renders the profile page and form
    """
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileRegisterForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile has been successfully updated.')
            return redirect('accounts:profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileRegisterForm(instance=request.user.profile)

    context = {
        'title': 'Accounts',
        'nbar': 'accounts',
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)
