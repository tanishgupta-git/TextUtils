#created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {'name': 'tanish', 'position': "founder"}
    return render(request, 'index.html')
    # return HttpResponse("hello")

def analyze(request):
    djtext = request.POST.get('text', "default")
    removepunc = request.POST.get('removepunc', 'off')
    fullcapitalize = request.POST.get('fullcapitalize', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    charcount = request.POST.get('charcount', 'off')
    extraspaceremove = request.POST.get('extraspaceremove', 'off')
    if  (removepunc == 'on' or fullcapitalize == 'on' or newlineremove == 'on' or charcount == 'on' or extraspaceremove == 'on'):
        purposedynamic = '  '
        seconditer = djtext

        if removepunc == "on":
            analyzed = ""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in seconditer:
                if char not in punctuations:
                    analyzed = analyzed + char
            seconditer = analyzed
            purposedynamic = purposedynamic + 'Removed Punctions  '

        if fullcapitalize == "on":
            analyzed = ""
            for char in seconditer:
                analyzed = analyzed + char.capitalize()
            seconditer = analyzed
            purposedynamic = purposedynamic + 'Full Capitalize  '

        if newlineremove == 'on':
            analyzed = ""
            for char in seconditer:
                if char != '\n' and char != '\r':
                    analyzed = analyzed + char
            seconditer = analyzed
            purposedynamic = purposedynamic + 'remove the new line  '

        if extraspaceremove == 'on':
            analyzed = ""
            for index,char in enumerate(seconditer):
                if not(djtext[index] == ' ' and (index != len(seconditer)-1) and djtext[index+1] == ' '):
                    analyzed = analyzed + char
            seconditer = analyzed
            purposedynamic = purposedynamic + 'ExtraSpace remover  '
        params = {'purpose': purposedynamic, 'analyzed_text': analyzed, 'count_text': " "}
        if charcount == 'on':
            counting = len(djtext)
            purposedynamic = purposedynamic + 'Characters count  '
            params = { 'purpose': purposedynamic, 'analyzed_text': analyzed, 'count_text':f"Total Character in text are {counting}"}

        return render(request, 'analyze.html',  params)
    else:
        return HttpResponse("Error")