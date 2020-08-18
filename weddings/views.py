from django.shortcuts import render
from django.http import HttpResponse
def 03_regular_page(request):
   return render(request, '03_regular_page.html')


def index(request):
    return render(request, 'index.html')


def 02_rsvp(request):
    return render(request, '02_rsvp.html')




