from django.conf.urls import url
from ..views import (BookListView, BookCreateView, BookDetailView,
                     BookUpdateView, BookDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(BookCreateView.as_view()),
        name="book_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(BookUpdateView.as_view()),
        name="book_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(BookDeleteView.as_view()),
        name="book_delete"),

    url(r'^(?P<pk>\d+)/$',
        BookDetailView.as_view(),
        name="book_detail"),

    url(r'^$',
        BookListView.as_view(),
        name="book_list"),
]
