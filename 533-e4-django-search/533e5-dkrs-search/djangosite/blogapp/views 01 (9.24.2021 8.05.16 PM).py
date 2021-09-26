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

    # https://stackoverflow.com/questions/13416502/django-search-form-in-class-based-listview
    #
    # works..
    # see supertramp
    def off01_get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.all()
        return object_list

    # error: 'NoneType' object has no attribute '_meta'
    def off02_get_queryset(self):
        fields = [m.name for m in super(PostListView, self).model._meta.fields]
        result = super(PostListView, self).get_queryset()
        query = self.request.GET.get('q')
        if query:
            result = result.filter(
                reduce(lambda x, y: x | Q(**{"{}__icontains".format(y): query}), fields, Q())
            )
        return result
        

    # https://stackoverflow.com/questions/53032675/django-listview-with-filter-option-like-djangoadmin  
    
    # error:
    # djdev_1     |     adm_model = PostAdmin(Post,AdminSite())
    # djdev_1     | NameError: name 'PostAdmin' is not defined

    adm_model = PostAdmin(Post,AdminSite()) 
    changelist = None        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.changelist = self.adm_model.get_changelist_instance(self.request)
        context['cl']=self.changelist 
        return context

    def off3_get_queryset(self):
        qs = super().get_queryset()
        get_params = self.request.GET.dict()

        self.changelist = self.adm_model.get_changelist_instance(self.request)

        (self.changelist.filter_specs, self.changelist.has_filters, remaining_lookup_params,
         filters_use_distinct) = self.changelist.get_filters(self.request)

        # Then, we let every list filter modify the queryset to its liking.
        qs = self.changelist.root_queryset
        for filter_spec in self.changelist.filter_specs:
            new_qs = filter_spec.queryset(self.request, qs)
            if new_qs is not None:
                qs = new_qs
        try:
            qs = qs.filter(**remaining_lookup_params)
        except:
            pass

        # Set ordering.
        ordering = self.changelist.get_ordering(self.request, qs)
        qs = qs.order_by(*ordering)

        # Apply search results
        qs, search_use_distinct = self.changelist.model_admin.get_search_results(self.request, qs, self.changelist.query)

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
        

