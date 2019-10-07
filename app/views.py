from django.shortcuts import render


def home(request):
    context = {
        "title": "Somos Todos",
    }
    return render(request, 'app/base.html', context=context)