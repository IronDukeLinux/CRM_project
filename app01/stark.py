# '2018/8/28 17:19'
# coding=utf-8


from stark.service.sites import site, ModelStark
from app01.models import Book, Publish, Author, AuthorDetail
from django.utils.safestring import mark_safe
from django.urls import reverse
from django import forms

# class BookConfig(ModelStark):
#     """
#     自己定义的配置类，但是只会重写部分方法和属性
#     所以需要继承默认的配置类
#     """
#     def edit(self, obj=None, is_header=False):
#         if is_header:
#             return '编辑书籍'
#         else:
#             print(reverse('app01_book_query_list'))
#             print(reverse('app01_publish_query_list'))
#             print(reverse('app01_author_add_data'))
#             print(reverse('app01_author_delete_data', args=(1, )))
#             return mark_safe("<a href='/stark/app01/book/%s/change/'>编辑</a>" % obj.pk)
#
#     def dele(self, obj=None, is_header=False):
#         if is_header:
#             return '删除书籍'
#         else:
#             return mark_safe("<a href='/stark/app01/book/%s/delete/'>删除</a>" % obj.pk)
#
#     list_display = ["title", "price", "publish", "authors", edit, dele]


class BookModelForm(forms.ModelForm):
    class Meta:
        val = {"required": "字段不能为空"}
        model = Book
        fields = "__all__"
        labels = {
            "title": "书名",
            "price": "价格",
        }
        error_messages = {
            "title": val,
            "price": val,
        }


class BookConfig(ModelStark):
    model_form_class = BookModelForm
    list_display = ["title", "price", "publish", "authors"]
    list_display_links = ["title", ]
    search_fields = ["title", ]

    # 过滤功能
    list_filter = ["publish", "authors"]

    # 批量操作
    def patch_init(self, queryset):
        queryset.update(price=0)
    patch_init.desc = "价格初始化"
    action_fields = [patch_init, ]
# Book.objects.filter(title__icontains=)


site.register(Book, BookConfig)
site.register(Publish)
site.register(Author)
site.register(AuthorDetail)
