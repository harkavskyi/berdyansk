from django.shortcuts import render


# Create your views here.


def ru(request):
    return render(request, 'main_ru.html')


def ukr(request):
    return render(request, 'main_ukr.html')
