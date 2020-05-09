from django.shortcuts import render
from marketing.forms import EmailSubscribeForm

from .calculator import Calculator


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
    if request.method == 'POST':
        user_inputs = request.POST
        fields = ['weight', 'height', 'age', 'pal', 'goal', 'gender', 'height_unit', 'weight_unit']
        user_form = {user_input: user_inputs[user_input] for user_input in fields if user_input in user_inputs.keys()}
        context['user_form'] = user_form
        context['results'] = Calculator(user_form).results()

    return render(request, 'calculator/index.html', context)
