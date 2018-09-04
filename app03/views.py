from django.shortcuts import render
from app03.models import Book
from app03.page import MyPage
# Create your views here.


def index(request):

    # 创建数据
    # li = [Book(title='python_%s' % i, price=i*i) for i in range(1, 101)]
    # Book.objects.bulk_create(li)
    page_num = request.GET.get('page', 1)
    data_list = Book.objects.all()
    page_obj = MyPage(page_num, data_list.count(), request)
    data_list = data_list[page_obj.start: page_obj.end]

    return render(request, "index.html", locals())
