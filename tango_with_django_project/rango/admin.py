from django.contrib import admin
from rango.models import Category, Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')  #让管理主页里的page行能显示title cate url

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

