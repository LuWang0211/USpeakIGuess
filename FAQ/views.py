from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.
# def FAQView(request):
#     return HttpResponse('Frequently Asked Questions')

def FAQView(request):
    return render(request, 'faq.html')