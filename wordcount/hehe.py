import operator

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def raj(request):
    return HttpResponse('<h1>Shobhit Raj</h1>')


def count(request):
    text = request.GET['Text']
    list = text.split()
    worddict = {}
    for word in list:
        if word in worddict:
            worddict[word] +=1
        else:
            worddict[word] = 1
    sort = sorted(worddict.items(),key= operator.itemgetter(1),reverse=True)
    return render(request, 'count.html', {'text': text , 'count':len(list), 'worddict': sort})

def about(request):
    return render(request, 'about.html')