from django.shortcuts import render
from .models import Articles
from django.core.paginator import Paginator

# Create your views here.

# FBV  function based view   基于函数的视图
def index(request):
    '''
        文章列表页
    '''
    return render(request,'index.html')


def detail(request,pk):
    '''
        文章列表页
    '''
    return render(request,'single_article.html')


def contact(request):
    '''
        联系我们
    '''
    return render(request,'contact.html')


def about(request):
    '''
        关于我
    '''
    return render(request,'about.html')



