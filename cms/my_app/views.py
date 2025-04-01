from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Author, Category

import json

def homepage(request):
    articles = Article.objects.order_by('title')
    return render(request, 'content/homepage.html', {'articles': articles})


def article(request, id):
    article = Article.objects.get(pk=id)

    return render(request, 'content/article.html', {'article': article})

def author(request, id):
    author = Author.objects.get(pk=id)
    return render(request, 'content/author.html', {'author': author})

def category(request, id):
    category = Category.objects.get(pk=id)
    return render(request, 'content/category.html', {'category': category})