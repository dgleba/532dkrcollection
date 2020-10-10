from django.shortcuts import render

# Create your views here.

# # tutorial/views.py
# from django.views.generic import ListView
# from .models import Person

# class PersonListView(ListView):
#     model = Person
#     template_name = 'contactapp/people.html'


# tutorial/views.py
from django_tables2 import SingleTableView

from .models import Person
from .tables import PersonTable


class PersonListView(SingleTableView):
    model = Person
    table_class = PersonTable
    template_name = 'contactapp/people.html'    