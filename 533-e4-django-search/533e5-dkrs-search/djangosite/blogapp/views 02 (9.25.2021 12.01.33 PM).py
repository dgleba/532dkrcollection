from django.contrib import admin
from django.views import generic
from . import models
from . import forms
from . import admin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm
    paginate_by = 5

    # https://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview -- # see supertramp
    #
    # works..
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


    # https://stackoverflow.com/questions/53032675/django-listview-with-filter-option-like-djangoadmin
    # error noworky...
    def off2_get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()
        # search
        if get_params.get('q') and hasattr(self, 'search_fields'):
            # logic for search goes here....
        # filter
        # if hasattr(self, 'list_filter'):
        #     filter_fields = self.list_filter
        #     for key, value in get_params.items():
        #         if key in filter_fields and key != 'q' and value != '':
        #             qs = qs.filter(**{key:value})
            return qs


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(LoginRequiredMixin,PermissionRequiredMixin,generic.UpdateView):
    permission_required = ('blogapp.change_post',  )
    permission_classes = (IsAuthenticated,)
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World dg.'}
        return Response(content)
        

