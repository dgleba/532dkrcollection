from django.db import models
from django.urls import reverse


class Book(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=30)
    author = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("blogapp_Book_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("blogapp_Book_update", args=(self.pk,))

    # https://www.edureka.co/community/79338/choose-value-label-from-django-modelchoicefield-queryset
    # ModelChoiceField NameError: name 'Book' is not defined
    def __unicode__(self):
        return self.name


class Post(models.Model):

    # Relationships
    book = models.ForeignKey("blogapp.Book", on_delete=models.CASCADE)

    # Fields
    body = models.TextField(max_length=32100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=230)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("blogapp_Post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("blogapp_Post_update", args=(self.pk,))

