from django.shortcuts import render, HttpResponse
from datetime import datetime
import random

def index(request):
    return render(request, 'index.html')

def day_of_week(request):
    day = datetime.now().strftime("%A")
    return HttpResponse("Day of the week is: " + day)

def random_quote(request):
    quotes = [
        'The best way to get started is to quit talking and begin doing. - Walt Disney',
        'If two wrongs dont make a right, try three. - Laurence J. Peter',
        'Get your facts first, then you can distort them as you please. - Mark Twain',
        'A day without sunshine is like, you know, night. - Steve Martin',
        'My fake plants died because I did not pretend to water them. - Mitch Hedberg',
        'Funny quote. - Some Guy'
    ]
    choice = random.choice(quotes)
    return HttpResponse(choice)

def data(request):
    first_name = None
    last_name = None
    if request.method == "POST":
        first_name = request.POST.get("name")
        last_name = request.POST.get("lastname")
    print(first_name, last_name)
    return render(request, "data.html", {first_name, last_name})

def news(request):
    return render(request, 'news.html')

def about_us(request):
    return render(request, 'about.html')

def branch(request):
    return render(request, 'branches/details.html')

def custom_error(request, exception):
    return render(request, '404.html', status=404)

