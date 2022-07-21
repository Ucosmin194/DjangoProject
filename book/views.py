from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

from book.filters import BookFilter
from book.forms import BookForm
from book.models import Book


class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'book/create_new_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('create_new_book')
    permission_required = 'book.add_book'


class BookListView(LoginRequiredMixin, ListView):
    template_name = 'book/list_of_books.html'
    model = Book
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.filter(active=True)

    def get_context_data(self,  **kwargs):
        data = super(BookListView, self).get_context_data()
        # all_teachers = Teacher.objects.all()
        # data['teachers'] = all_teachers
        books = Book.objects.all()
        myFilter = BookFilter(self.request.GET, queryset=books)
        data['all_books'] = myFilter.qs
        data['myFilter'] = myFilter

        return data


class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = 'book/update_book.html'
    model = Book
    form_class = BookForm
    success_url = reverse_lazy('list_of_books')
    permission_required = 'book.change_book'


class BookDetailView(LoginRequiredMixin, DetailView):
    template_name = 'book/details_book.html'
    model = Book


class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'book/delete_book.html'
    model = Book
    success_url = reverse_lazy('list_of_books')
    permission_required = 'book.delete_book'


@login_required
def out_of_stock_book(request, pk):
    Book.objects.filter(id=pk).update(is_in_stock=False)
    return redirect('list_of_books')

