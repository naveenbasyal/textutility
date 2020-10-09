#I have created this file "Naveen Basyal"
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return HttpResponse("Home")
    return render(request, 'index.html')

def analyze(request):

    # Get the text
    djtext = request.POST.get("text1", "default")
    removepunc= request.POST.get('removepunc','off')
    charactercount= request.POST.get('charactercount','off')
    fullcaps= request.POST.get('fullcaps','off')
    RemoveExtraSpace= request.POST.get('RemoveExtraSpace','off')

#which checkbox is on
    if removepunc=="on":
         punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed=""
         for char in djtext:
             if char not in punctuations:
                 analyzed = analyzed + char
         params={ 'params':'Punctuation Removed','analyzed_text' : analyzed }
         return render(request, 'analyze.html', params)

    elif(charactercount=="on"):
        analyzed=0
        for char in djtext:
         analyzed+=1
        params = {'params':'Character Counted','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'params':'Changed to UpperCase','analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif (RemoveExtraSpace == "on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]==" ":
                pass
            else:
              analyzed = analyzed + char
        params = {'params': 'Extra Space Removed', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return render(request, 'analyzed2.html')

