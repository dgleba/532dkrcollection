# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# import django.urls to set absolute URL
from django.urls import reverse


class Blog(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    
    # timestamps
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    book = models.ForeignKey("blog.Book", on_delete=models.CASCADE)

    # Inspect Blog object via name
    def __str__(self):
        return self.title

    # Inspect absolute Blog object's URL
    def get_absolute_url(self):
        return reverse('blog_edit', kwargs={'pk': self.pk})

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)

    # It's always fine knowing when it is created
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    # Inspect Book object via name
    def __str__(self):
        return self.name

    # Inspect absolute Book object's URL
    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})

                