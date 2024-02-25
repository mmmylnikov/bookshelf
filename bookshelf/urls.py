from django.contrib import admin
from django.urls import path, include

from books.views import (
    books_view, book_detail_view,
    api_get_books, api_get_book_detail,
    )

urlpatterns = [
    path("__debug__/", include("debug_toolbar.urls")),
    path('admin/', admin.site.urls),
    path('books/', books_view, name='books_view'),
    path('books/<int:book_id>/', book_detail_view, name='book_detail_view'),
    path('api/books/', api_get_books),
    path('api/books/<int:book_id>/', api_get_book_detail),
]
