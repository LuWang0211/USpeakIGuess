from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _


# from django.http import HttpResponse
from .models import FAQItems

# Create your views here.
# def FAQView(request):
#     return HttpResponse('Frequently Asked Questions')

def FAQView(request):
    all_faq_items = FAQItems.objects.all()

    important_text = _('lulu is small guaiguai')

    print(important_text)
    
    # all_FAQ_items ='cd  FAQItems.objects.all()'
    return render(request, 'faq.html', {'all_faqitems': all_faq_items, 'important_text': important_text})

def addQuestion(request):
    new_item = request.GET['content']
    new_FAQ_item = FAQItems(content=new_item)
    new_FAQ_item.save()
    return HttpResponseRedirect('/faq/')

def deleteQuestion(request, faqitem_id):
    FAQ_item_toDelete = FAQItems.objects.get(id=faqitem_id)
    FAQ_item_toDelete.delete()
    return HttpResponseRedirect('/faq/')
