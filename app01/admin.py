from django.contrib import admin

# Register your models here.
from app01.models import Book, AuthorDetail, Author, Publish


class BookConfig(admin.ModelAdmin):
    list_display = ["title", "price"]
    search_fields = ["title", ]
    list_filter = ["publish", "authors"]


admin.site.register(Book, BookConfig)
admin.site.register(Author)
admin.site.register(AuthorDetail)
admin.site.register(Publish)
