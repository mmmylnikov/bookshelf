from django.shortcuts import render, redirect
from django.core import serializers
from django.http import (
    HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseNotFound,
    JsonResponse)
import json

from books.models import Book


def books_view(request: HttpRequest) -> HttpResponse:
    books = Book.objects.all()
    return render(request, 'books/books.html', context={'books': books})


def book_detail_view(
        request: HttpRequest, book_id: int
        ) -> HttpResponse | HttpResponseRedirect:
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        return redirect('books_view', permanent=False)
    return render(request, 'books/book_detail.html', context={'book': book})


def api_get_books(request: HttpRequest) -> JsonResponse:
    books_json_str = serializers.serialize("json", Book.objects.all())
    data = json.loads(books_json_str)
    return JsonResponse(data=data, safe=False, json_dumps_params={'indent': 4})


def api_get_book_detail(
        request: HttpRequest, book_id: int
        ) -> JsonResponse | HttpResponseNotFound:
    try:
        book = Book.objects.get(id=book_id)
        book_json_str = serializers.serialize("json", [book])[1:-1]
        data = json.loads(book_json_str)
        return JsonResponse(
            data=data, safe=False, json_dumps_params={'indent': 4})
    except Book.DoesNotExist:
        return HttpResponseNotFound()
