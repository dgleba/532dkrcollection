from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from ..models import Book
from ..forms import BookForm
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import Http404


class BookListView(ListView):
    model = Book
    template_name = "blogapp/book_list.html"
    paginate_by = 20
    context_object_name = "book_list"
    allow_empty = True
    page_kwarg = 'page'
    paginate_orphans = 0

    def __init__(self, **kwargs):
        return super(BookListView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BookListView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BookListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return super(BookListView, self).get_queryset()

    def get_allow_empty(self):
        return super(BookListView, self).get_allow_empty()

    def get_context_data(self, *args, **kwargs):
        ret = super(BookListView, self).get_context_data(*args, **kwargs)
        return ret

    def get_paginate_by(self, queryset):
        return super(BookListView, self).get_paginate_by(queryset)

    def get_context_object_name(self, object_list):
        return super(BookListView, self).get_context_object_name(object_list)

    def paginate_queryset(self, queryset, page_size):
        return super(BookListView, self).paginate_queryset(queryset, page_size)

    def get_paginator(self, queryset, per_page, orphans=0, allow_empty_first_page=True):
        return super(BookListView, self).get_paginator(queryset, per_page, orphans=0, allow_empty_first_page=True)

    def render_to_response(self, context, **response_kwargs):
        return super(BookListView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BookListView, self).get_template_names()


class BookDetailView(DetailView):
    model = Book
    template_name = "blogapp/book_detail.html"
    context_object_name = "book"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'

    def __init__(self, **kwargs):
        return super(BookDetailView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BookDetailView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BookDetailView, self).get(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BookDetailView, self).get_object(queryset)

    def get_queryset(self):
        return super(BookDetailView, self).get_queryset()

    def get_slug_field(self):
        return super(BookDetailView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(BookDetailView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BookDetailView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BookDetailView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BookDetailView, self).get_template_names()


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    # fields = ['author', 'title']
    template_name = "blogapp/book_create.html"
    success_url = reverse_lazy("book_list")

    def __init__(self, **kwargs):
        return super(BookCreateView, self).__init__(**kwargs)

    def dispatch(self, request, *args, **kwargs):
        return super(BookCreateView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BookCreateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(BookCreateView, self).post(request, *args, **kwargs)

    def get_form_class(self):
        return super(BookCreateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(BookCreateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(BookCreateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(BookCreateView, self).get_initial()

    def form_invalid(self, form):
        return super(BookCreateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(BookCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(BookCreateView, self).get_context_data(**kwargs)
        return ret

    def render_to_response(self, context, **response_kwargs):
        return super(BookCreateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BookCreateView, self).get_template_names()

    def get_success_url(self):
        return reverse("blogapp:book_detail", args=(self.object.pk,))


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    # fields = ['author', 'title']
    template_name = "blogapp/book_update.html"
    initial = {}
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "book"

    def __init__(self, **kwargs):
        return super(BookUpdateView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BookUpdateView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super(BookUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super(BookUpdateView, self).post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BookUpdateView, self).get_object(queryset)

    def get_queryset(self):
        return super(BookUpdateView, self).get_queryset()

    def get_slug_field(self):
        return super(BookUpdateView, self).get_slug_field()

    def get_form_class(self):
        return super(BookUpdateView, self).get_form_class()

    def get_form(self, form_class=None):
        return super(BookUpdateView, self).get_form(form_class)

    def get_form_kwargs(self, **kwargs):
        return super(BookUpdateView, self).get_form_kwargs(**kwargs)

    def get_initial(self):
        return super(BookUpdateView, self).get_initial()

    def form_invalid(self, form):
        return super(BookUpdateView, self).form_invalid(form)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()
        return super(BookUpdateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        ret = super(BookUpdateView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BookUpdateView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BookUpdateView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BookUpdateView, self).get_template_names()

    def get_success_url(self):
        return reverse("blogapp:book_detail", args=(self.object.pk,))


class BookDeleteView(DeleteView):
    model = Book
    template_name = "blogapp/book_delete.html"
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
    pk_url_kwarg = 'pk'
    context_object_name = "book"

    def __init__(self, **kwargs):
        return super(BookDeleteView, self).__init__(**kwargs)

    def dispatch(self, *args, **kwargs):
        return super(BookDeleteView, self).dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        raise Http404

    def post(self, request, *args, **kwargs):
        return super(BookDeleteView, self).post(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(BookDeleteView, self).delete(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return super(BookDeleteView, self).get_object(queryset)

    def get_queryset(self):
        return super(BookDeleteView, self).get_queryset()

    def get_slug_field(self):
        return super(BookDeleteView, self).get_slug_field()

    def get_context_data(self, **kwargs):
        ret = super(BookDeleteView, self).get_context_data(**kwargs)
        return ret

    def get_context_object_name(self, obj):
        return super(BookDeleteView, self).get_context_object_name(obj)

    def render_to_response(self, context, **response_kwargs):
        return super(BookDeleteView, self).render_to_response(context, **response_kwargs)

    def get_template_names(self):
        return super(BookDeleteView, self).get_template_names()

    def get_success_url(self):
        return reverse("blogapp:book_list")
