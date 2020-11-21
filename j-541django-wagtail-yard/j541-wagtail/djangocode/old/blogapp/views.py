from django.views import generic
from . import models
from . import forms


class BookListView(generic.ListView):
    model = models.Book
    form_class = forms.BookForm


class BookCreateView(generic.CreateView):
    model = models.Book
    form_class = forms.BookForm


class BookDetailView(generic.DetailView):
    model = models.Book
    form_class = forms.BookForm


class BookUpdateView(generic.UpdateView):
    model = models.Book
    form_class = forms.BookForm
    pk_url_kwarg = "pk"


class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"
