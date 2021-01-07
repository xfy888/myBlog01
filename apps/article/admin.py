from django.contrib import admin
from .models import Articles,Category,Tag
from markdownx.widgets import AdminMarkdownxWidget
from django.db import models

# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMarkdownxWidget},
    }

    # 希望显示的字段
    # fields=("title","author","content")
    # 除去某一字段
    # exclude=("img",)
    # 表头
    list_display=("title","author","img","abstract","visited","created_at","cmodidied_at")
    # 搜索
    search_fields=("title","abstract","content")
    # 筛选条件
    # list_filter=list_display
    list_filter=("title",)


admin.site.register(Articles,ArticlesAdmin)
admin.site.register(Category,)
admin.site.register(Tag,)