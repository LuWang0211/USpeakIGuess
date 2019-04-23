from django.shortcuts import render
from django.http import HttpResponseRedirect
# from AuthorIdentification.inputoutput import input_output  #test tmp
from AuthorIdentification.Deltamethod import deltamethod  #test tmp
from django.core.files.base import ContentFile # save input_text into a file
import io, os

# Create your views here.
def AuthorIdView(request):
    #test tmp import
    user_input_test=""
    IdentifyResult=('','Please enter text to be authenticated. ')
    if request.POST:
        user_input_test=request.POST.get('user_input_test', '')

        curren_path = os.getcwd()
        print(curren_path)
        txt_file = open(f"{curren_path}/AuthorIdentification/test.txt", "w")
        txt_file.write(user_input_test)
        txt_file.close()

        #test tmp import
        # IdentifyResult=input_output(user_input_test)
        IdentifyResult=deltamethod('test.txt')
        # print(type(IdentifyResult))
        # print(IdentifyResult[0])
    return render(request, 'AuthorIdentification.html', {'resp_0': IdentifyResult[0],'resp_1': IdentifyResult[1],'user_input_test':user_input_test})

def Identify(request):
    # new_test_item = AuthorIditem(content=test_item)
    # new_test_item.save()
    # return HttpResponseRedirect('/AuthorIdentification/')
    #test tmp import
    # user_input_test=""
    # IdentifyResult="before test"
    # if request.POST:
    #     user_input_test=request.POST.get('user_input_test', '')
    #     #test tmp import
    #     IdentifyResult=input_output(user_input_test)
    # return render(request, 'AuthorIdentification.html', {'resp': IdentifyResult, 'user_input_test':user_input_test})
    return HttpResponseRedirect('/AuthorIdentification/')

def Backhome(request):
    return HttpResponseRedirect('/home/')
