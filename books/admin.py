from django.contrib import admin
from .models import Author, Book
# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_first_name', 'author_last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_title', 'book_author', 'book_published_date')