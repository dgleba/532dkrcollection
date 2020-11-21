# from django.shortcuts import render

# # Create your views here.

# # tutorial/views.py
# from django.views.generic import ListView
# from .models import Person

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

# tutorial/views.py
from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable

import django_filters
from django.db import models

# class PersonListView(SingleTableView):
#     model = Person
#     table_class = PersonTable
#     template_name = 'tutorial/people.html'    



class PersonFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='ch_filter', label='search text fields')

    # https://stackoverflow.com/questions/53828883/django-filter-i-want-to-filter-in-different-attributes-with-just-one-filter-in   
    # "django-filter" all character fields with one input
    # https://stackoverflow.com/questions/49791282/django-filter-how-to-change-placeholder-to-remplace-invalid-name
    # https://stackoverflow.com/questions/31686157/django-set-filter-field-label-or-verbose-name

    class Meta:
        model = Person

        # https://rpkilby.github.io/django-filter/usage.html
        filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_expr': 'icontains',
                },
            },
        }
        fields = ['q', ]
        exclude = ['password','created_at','updated_at']   

        def __init__(self, *args, **kwargs):
                super(PersonFilter, self).__init__(*args, **kwargs)
                self.filters['q'].extra.update(
                    {'empty_label': 'All Manufacturers'})
                    
    def ch_filter(self, queryset, name, value):
            return queryset.filter(
                name__icontains=value
            ) | queryset.filter(
                place__icontains=value
            ) 
            
class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = PersonTable
    model = Person
    # template_name = "template.html"
    template_name = 'tutorial/people.html'    

    filterset_class = PersonFilter    

