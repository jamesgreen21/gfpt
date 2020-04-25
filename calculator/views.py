from django.shortcuts import render


def index(request):

    context = {
        'title': 'Calorie Calculator',
        'nbar': 'calc',
    }

    return render(request, 'calculator/index.html', context)
