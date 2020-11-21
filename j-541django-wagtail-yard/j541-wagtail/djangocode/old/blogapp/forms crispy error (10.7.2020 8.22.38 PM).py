from django import forms
from . import models

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.template.context_processors import csrf
from crispy_forms.utils import render_crispy_form

# i added this to address the error below.
# ModelChoiceField NameError: name 'Book' is not defined
from .models import Post, Book

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = [
            "name",
            "author",
        ]


""" class PostForm(forms.ModelForm):

    # https://www.edureka.co/community/79338/choose-value-label-from-django-modelchoicefield-queryset
    # ModelChoiceField NameError: name 'Book' is not defined
    # http://alexopoulos7.blogspot.com/2016/11/django-forms-choice-tutorial-sample-code.html
 
    # not sure all this crispy stuff is needed, as it worked without all this.

    # crispy forms..
    #  https://django-crispy-forms.readthedocs.io/en/latest/crispy_tag_forms.html   
    #  https://stackoverflow.com/questions/13098954/use-crispy-form-with-modelform
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        # self.helper.layout.append(Submit('save', 'save'))
        
    book = forms.ModelChoiceField(queryset=Book.objects.all())

    class Meta:
        model = models.Post
        fields = [
            "body",
            "title",
            "book",
        ]
"""



class PostForm(forms.Form):
    title = forms.CharField()
    body = forms.CharField()
    
    # helper.form_class = 'form-horizontal'
    # helper.label_class = 'col-lg-2'
    # helper.field_class = 'col-lg-8'
    # helper.layout = Layout(
    #     'title',
    #     'body',
    #     StrictButton('submit', css_class='btn-default'),
    # )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-postForm'
        self.helper.form_class = 'blueForms'
        self.helper.form_method = 'post'
        self.helper.form_action = 'submit_post'

        self.helper.add_input(Submit('submit', 'Submit'))


