from django.shortcuts import render


def country_index(request):
    return render(request, 'index.html')