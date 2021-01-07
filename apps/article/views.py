from django.shortcuts import render
from .models import Articles,Category,Tag
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

# FBV  function based view   基于函数的视图
def index(request):
    '''
        文章列表页
    '''
    # articles = Articles.objects.all().order_by('created_at')
    articles = Articles.objects.all()
    #每页上的条数限制为两条进行分页
    limited = 2
    p=Paginator(articles,limited)
    # 得到前端传过来的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1

    articles = p.get_page(page)

    # 获取到最新的5篇文章
    lastest_articles =articles[::]
    #获取所有的分类
    categories = Category.objects.all()
    #获取所有的标签
    tags = Tag.objects.all()
    context = {
        "articles":articles,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags,
    }
    return render(request,'index.html',context)


def detail(request,pk):
    '''
        文章列表页
    '''
    article = Articles.objects.get(pk=pk)
    article.increace_visited()
    print(article.get_absolute_url())
    # 获取到最新的5篇文章
    lastest_articles = Articles.objects.all()[:3]
    #获取所有的分类
    categories = Category.objects.all()
    #获取所有的标签
    tags = Tag.objects.all()
    context = {
        'article':article,
        "lastest_articles":lastest_articles,
        "categories":categories,
        "tags":tags,
    }
    return render(request,'single_article.html',context)



def search(request):
    keyword=request.GET.get("keyword")
    print('keyword=',keyword)
    if not keyword:
        error_msg = '请输入关键字'
        return render(request,'index.html',locals())
    articles = Articles.objects.filter(Q(title__icontains = keyword)|Q(abstract__icontains = keyword)|Q(content__icontains=keyword))
    limited=2
    p=Paginator(articles,limited)
    # 传到前端穿过的page参数
    try:
        page = request.GET.get('page',1)
    except PageNotFound:
        page = 1

    articles = p.get_page(page)

    lasted_articles=articles[:3]
    # 实例化Category并且获取所有的是数据和内容
    category=Category.objects.all()
    #实例化Tag并且获取所有数据和内容
    tags = Tag.objects.all()
    return render(request,'index.html',locals())


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



