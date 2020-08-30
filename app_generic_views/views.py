from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from app_generic_views.models import BookCategory
from books.models import Book


def get_books_categories():
    BooksCategories = []
    for catgory in BookCategory.objects.all().order_by("category_name"):
        BooksCategories.append({"id": catgory.id, "category_name": catgory.category_name})
    return BooksCategories

class BookList(ListView):
    model = Book
    # template_name is optional, by default it will books/book_list.html
    template_name = "app_generic_views/book_list.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Books List"
        kwargs["page"] = "BooksList"
        return super().get_context_data(**kwargs)


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')
    # template_name is optional, by default it will books/book_list.html
    template_name = "app_generic_views/book_entry.html"

    def get_context_data(self, **kwargs):
        kwargs["title"] = "Add New Book"
        kwargs["page"] = "NewBook"
        kwargs["BooksCategories"] = get_books_categories()

        return super().get_context_data(**kwargs)