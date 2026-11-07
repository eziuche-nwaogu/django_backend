from django.urls import path, include
from  . import views

urlpatterns = [
    path('books/', views.books_list, name='books-list'),
    path('authors/', views.authors_list, name='authors-list'),

    # api detail views
    path('books/<int:pk>/', views.book_detail, name='book-detail'),
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
]