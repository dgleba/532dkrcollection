from django.contrib import admin
from django.views import generic
from . import models
from . import forms
from . import admin

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin



# https://stackoverflow.com/questions/21137821/using-django-admin-search-engine-in-my-own-views
# from django.db.models import Q
# from django.db.models.query import QuerySet
# import operator

def django_admin_keyword_search(model, keywords, base_qs=None):
    """Search according to fields defined in Admin's search_fields"""
    if not keywords: 
        return []
    fields = model._meta.admin.search_fields

    qs = QuerySet(model)

    for keyword in keywords:
        or_queries = [Q(**{'%s__icontains' % field: keyword}) for field in fields]
        if base_qs is None:
            other_qs = QuerySet(model)
        else:
            other_qs = base_qs
        if qs._select_related:
            other_qs = other_qs.select_related()
        other_qs = other_qs.filter(reduce(operator.or_, or_queries))
        qs = qs & other_qs

    return qs

def do_keyword_search(model, query, base_qs=None):
    return django_admin_keyword_search(model, query.split(' '),
                                       base_qs=base_qs)


# =================================================

class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm
    paginate_by = 5

    # https://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview -- # see supertramp
    #
    # works..
    def off0_get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list


    # https://stackoverflow.com/questions/21137821/using-django-admin-search-engine-in-my-own-views
    #
    # error:
    # Exception Value:	'Options' object has no attribute 'admin'
    #
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # object_list = self.model.objects.filter(title__icontains=query)
            do_keyword_search(models.Post, query)
        else:
            object_list = self.model.objects.all()
        return object_list






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
        

