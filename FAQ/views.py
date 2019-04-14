from django.shortcuts import render
from django.http import HttpResponseRedirect

# from django.http import HttpResponse
from .models import FAQItems

# Create your views here.
# def FAQView(request):
#     return HttpResponse('Frequently Asked Questions')

def FAQView(request):
    all_faq_items = FAQItems.objects.all()
    # all_FAQ_items ='cd  FAQItems.objects.all()'
    return render(request, 'faq.html', {'all_faqitems': all_faq_items})

def addQuestion(request):
    new_item = request.GET['content']
    new_FAQ_item = FAQItems(content=new_item)
    new_FAQ_item.save()
    return HttpResponseRedirect('/faq/')

def deleteQuestion(request, faqitem_id):
    FAQ_item_toDelete = FAQItems.objects.get(id=faqitem_id)
    FAQ_item_toDelete.delete()
    return HttpResponseRedirect('/faq/')
