from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest
from django.http import HttpResponse


def index(request):

    context = {
        'name':'马上双11了，想要惊喜吗？'
    }
    # return HttpResponse("ok")
    return render(request, 'book/index.html', context)

"""
from book.models import BookInfo

增加数据：
方式1：
book = BookInfo(
        name='django',
        pub_date='2000-1-1',
        readcount=1
)
book.save()

方式2：
BookInfo.objects.create(
        name='django',
        pub_date='2000-1-1',
        readcount=1
)    


更新数据：
方式1：
book = BookInfo.objects.ger(id=6)
book.name = '哈哈哈'
book.save()

方式2：
BookInfo.objects.filter(id=5).update(name='嘿嘿嘿', commentcount=888)


删除数据：
方式1：
book=BookInfo.objects.get(id=2)
book.delete()

方式2：
BookInfo.objects.get(id=2).delete()
BookInfo.objects.filter(id=2).delete()
"""






