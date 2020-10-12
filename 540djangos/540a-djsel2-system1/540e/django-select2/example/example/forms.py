from django import forms

from django_select2 import forms as s2forms

from . import models


class AuthorWidget(s2forms.ModelSelect2Widget  ):
    search_fields = [ "email__icontains","username__icontains",]
    



class CoAuthorsWidget(s2forms.ModelSelect2MultipleWidget):
    search_fields = ["username__istartswith", "email__icontains"]


class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = "__all__"
        widgets = {
            "author": AuthorWidget (attrs = {"data-minimum-input-length": 0}) ,
            "co_authors": CoAuthorsWidget,
        }


