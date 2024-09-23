from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from.models import Book

# Create your views here.
class BookListView(ListView):
    model= Book
    template_name ='book_list.html'

class BookCreateView(CreateView):
    model= Book
    template_name ='book_form.html'
    fields=['title','author','description','published_date']
    success_url=reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model= Book
    template_name ='book_form.html'
    fields=['title','author','description','published_date']

class BookDeleteView(DeleteView):
    model= Book
    template_name ='book_confirm_delete.html'
    success_url=reverse_lazy('book_list')
    
class BookDetailView(DetailView):
    model= Book
    template_name ='book_detail.html'