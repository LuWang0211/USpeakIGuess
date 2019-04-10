from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def HomepageView(request):
    return HttpResponse('This is the Home page of USpeakIGuess!')
