from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from books.models import Book

class BookList(ListView):
    model = Book

'''
https://stackoverflow.com/questions/16268368/writing-a-django-detail-view-with-a-generic-class-based-view
https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/

When to use DetailView?

Django provides several class based generic views to accomplish common tasks. One among them is DetailView.

DetailView should be used when you want to present detail of a single model instance.

DetailView shouldn’t be used when your page has forms and does creation or update of objects. FormView, CreateView and UpdateView are more suitable for working with forms, creation or updation of objects.

Vanilla view can achieve everything which DetailView can, but DetailView has an advantage of avoiding a lot of boilerplate code which would be needed with View.

Let’s write a view by subclassing View and then modify the view to subclass DetailView. DetailView would help us avoid several lines of code and would also provide better separation of concern.
'''
class BookView(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['now'] = timezone.now()
        return context


class BookCreate(CreateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'pages']
    success_url = reverse_lazy('book_list')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book_list')