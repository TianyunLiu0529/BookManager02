from django.http import HttpResponse
from django.shortcuts import render
from book.models import BookInfo
# Create your views here.

def index(request):
    #在这里实现 增删改查

    books=BookInfo.objects.all()
    print(books)
    return HttpResponse('index')

