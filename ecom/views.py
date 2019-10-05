from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    # return render(request, 'ecom/home.html')
    return HttpResponse('<h1>This is the home page of this awesome website</h1>  <a href="/">Back</a>')


def index(request):
    # return HttpResponse('<h1>hello world</h1> <a href="/">Back</a>')
    context = {'name': 'tarun'}
    return render(request, 'ecom/index.html', context)

def removepunc(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    upp = request.GET.get('upper', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    countcharacter = request.GET.get('countcharacter', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == 'on':
        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in djtext:
            if char not in punctuation:
                   analyzed += char
            context = {'purpose': 'remove punctuations', 'final_output': analyzed}
    elif(upp == 'on'):
        analyzed = ''
        for char in djtext:
                analyzed += char.upper()
        context = {'purpose': 'uppar the characters', 'final_output': analyzed}
        return render(request, 'ecom/removepunc.html', context)

    elif(newlineremover == 'on'):
        analyzed = ''
        for char in djtext:
            if char != '\n':
                analyzed += char
        context = {'purpose': 'new line remover', 'final_output': analyzed}
        return render(request, 'ecom/removepunc.html', context)

        # elif(countcharacter == 'on'):
        #     analyzed = ''
        #     for char in djtext:
        #         analyzed += char.len()
        #
        #     context = {'purpose': 'new line remover', 'final_output': analyzed}
        #     return render(request, 'ecom/removepunc.html', context)

    elif(extraspaceremover == 'on'):
        analyzed = ''
        for char in djtext:
            ' '.join(char.split())
            analyzed += char
        context = {'purpose': 'new line remover', 'final_output': analyzed}
        return render(request, 'ecom/removepunc.html', context)


    else:
        return HttpResponse('ERROR')









# Create your views here.
