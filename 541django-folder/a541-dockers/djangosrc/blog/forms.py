# Import forms
from django import forms

from django_select2 import forms as s2forms

from .models import Blog


# for select2

class BookWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "name__icontains",
        "author__icontains",
    ]


class BlogForm(forms.ModelForm):

    # The solution originally retrieved from
    #
    # https://stackoverflow.com/questions/33452278/how-to-add-bootstrap-class-to-django-createview-form-fields-in-the-template
    #
    # Thanks to César

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {
            'class': 'form-control'
        }
        self.fields['body'].widget.attrs = {
            'class': 'form-control'
        }

    class Meta:
        model = Blog
        fields = ('__all__')
        widgets = {
            "book": BookWidget (attrs = {"data-minimum-input-length": 0}) ,
        }
