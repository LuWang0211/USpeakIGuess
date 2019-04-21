from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import AuthorIditem

# Create your views here.
def AuthorIdView(request):
    # return render(request, 'AuthorIdentification.html', {'most_likely_author': most_likely_author})
    return render(request, 'AuthorIdentification.html')

def Identify(request):
    test_item = request.GET['content']
    new_test_item = AuthorIditem(content=test_item)
    new_test_item.save()
    return HttpResponseRedirect('/AuthorIdentification/')

def Backhome(request):
    return HttpResponseRedirect('/home/')
