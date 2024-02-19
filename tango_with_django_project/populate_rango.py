import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [{'title': 'Official Python Tutorial', 
                     'url':'http://docs.python.org/3/tutorial/'},
                    {'title':'How to Think like a Computer Scientist',
                     'url':'http://www.greenteapress.com/thinkpython/'},
                    {'title':'Learn Python in 10 Minutes',
                     'url':'http://www.korokithakis.net/tutorials/python/'}]
    
    django_pages = [{'title':'Official Django Tutorial',
                     'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/'},
                    {'title':'Django Rocks',
                    'url':'http://www.djangorocks.com/'},
                    {'title':'How to Tango with Django',
                    'url':'http://www.tangowithdjango.com/'}]
    
    other_pages = [{'title':'Bottle',
                    'url':'http://bottlepy.org/docs/dev/'},
                    {'title':'Flask',
                    'url':'http://flask.pocoo.org'}]

    cats = {'python':{'pages':python_pages},                #这是个嵌套字典(pair)，cats是嵌套字典数组
            'Django':{'pages':django_pages},
            'Other Frameworks':{'pages':other_pages}}
    
    for cat, cat_data in cats.items():                    #cat是cats的键，cat_data是cats的值
        if cat == 'python':
            c = add_cat(cat,128,64)
        elif cat == 'Django':
            c = add_cat(cat,64,32)
        else:
            c = add_cat(cat,32,16)
        for p in cat_data['pages']:                       #cat_data['pages']是字典值，也就是pages字典(本质上是个嵌套嵌套字典，三重嵌套)
            add_page(c, p['title'], p['url'])
    
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}:{p}')
        





def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]  #get_or_create返回值是一个pair，0代表找到的对象，1是个布尔值
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, like):
    c = Category.objects.get_or_create(name=name, views=views,like=like)[0]
    c.views = views
    c.like = like
    c.save()
    return c
        
if __name__ == '__main__':                      #Python 中的一个常见用法，它用于判断当前脚本是否被直接执行
    print('Starting Rango population script...')
    populate()
