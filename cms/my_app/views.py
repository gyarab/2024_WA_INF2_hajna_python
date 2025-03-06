import json
from django.shortcuts import render
from django.http import HttpResponse
from my_app.models import Author, Book

# Create your views here.

def homepage(request):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)
        
    return render(request, 'my_app/homepage.html', {'articles': articles})
    
def article(request, id):
    with open('articles.json', encoding='utf-8') as f:
        articles = json.load(f)
        
    article = articles[id]
    return render(request, 'my_app/article.html', {'article': article})
    
def hello(request):
    return HttpResponse("Hello, Django!")

def vynasob(request, a, b):
    return HttpResponse(f'{a} * {b} = {a*b}')