from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect

# Create your views here.
def HomepageView(request):
    # return HttpResponse('This is the Home page of USpeakIGuess!')
    selected_language=''
    title='This is the Home page of USpeakIGuess!'
    gotoFAQ='FQA'
    gotoAId='AuthorIdentification'
    if request.method == "POST":
        selected_language=request.POST.get('selectelanguage')
        if selected_language=='en-us':
            title='Welcome the Home page of USpeakIGuess!'
            gotoFAQ='FQA'
            gotoAId='AuthorIdentification'
        elif selected_language=='zh-cn':
            title='欢迎来到“你说我猜”趣味语言分析平台!'
            gotoFAQ='常见问题'
            gotoAId='作者身份识别'
        print(title, selected_language)
    return render(request, 'home.html', {'title':title, 'FAQbuttonvalue':gotoFAQ, 'AIDbuttonvalue':gotoAId})

def FAQpage(request):
    return HttpResponseRedirect('/faq/')

def AuthorIdpage(request):
    return HttpResponseRedirect('/AuthorIdentification/')
