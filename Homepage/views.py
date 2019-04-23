from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def HomepageView(request):
    # return HttpResponse('This is the Home page of USpeakIGuess!')
    return render(request, 'home.html')

def FAQpage(request):
    return HttpResponseRedirect('/faq/')

def AuthorIdpage(request):
    return HttpResponseRedirect('/AuthorIdentification/')
