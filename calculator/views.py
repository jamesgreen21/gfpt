from django.shortcuts import render
from marketing.forms import EmailSubscribeForm


def index(request):
    """
    Creates a view for the Calculator App
    """
    subscribe_form = EmailSubscribeForm()
    context = {
        'title': 'Calorie Calculator',
        'nbar': 'calc',
        'subscribe_form': subscribe_form,
    }

    return render(request, 'calculator/index.html', context)

