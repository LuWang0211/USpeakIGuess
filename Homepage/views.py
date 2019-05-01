from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import activate, get_language, LANGUAGE_SESSION_KEY, gettext as _

# Create your views here.
def HomepageView(request):
    # return HttpResponse('This is the Home page of USpeakIGuess!')
    selected_language='en'
    if request.method == "POST":
        selected_language=request.POST.get('selectelanguage')
        if selected_language=='en' or selected_language=='zh':
            print(selected_language)

            # Only change the language if it is "en" or 'zh', disregard other values.
            activate(selected_language)

            # Also set session
            request.session[LANGUAGE_SESSION_KEY] = selected_language

    return render(request, 'home.html')

def FAQpage(request):
    return HttpResponseRedirect('/faq/')

def AuthorIdpage(request):
    return HttpResponseRedirect('/AuthorIdentification/')
