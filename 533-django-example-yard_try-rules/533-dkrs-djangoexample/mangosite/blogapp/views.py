from django.views import generic
from . import models
from . import forms

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin


from __future__ import absolute_import

from django.http import HttpResponse
from django.views.generic.edit import UpdateView, DeleteView, CreateView

from rules.contrib.views import permission_required, objectgetter
from rules.contrib.views import LoginRequiredMixin, PermissionRequiredMixin

# from .models import Book


class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(LoginRequiredMixin,generic.UpdateView):
    permission_classes = (IsAuthenticated,)
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World dg.'}
        return Response(content)
        