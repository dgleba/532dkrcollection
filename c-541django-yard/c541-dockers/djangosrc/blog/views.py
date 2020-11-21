# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Import Generic View for listing (r operation)
from django.views.generic import ListView, DetailView

# Import Generic View for creating, updating and deleting (cud operations)
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Resolving URLs
from django.urls import reverse_lazy

# Import Blog Model
from blog.models import Blog

# Import Blog Form
from blog.forms import BlogForm

# List View
class BlogList(ListView):
    model = Blog

# Detail View
class BlogView(DetailView):
    model = Blog

# Create View
class BlogCreate(CreateView):
    model = Blog
    form_class = BlogForm
    # Setting returning URL
    success_url = reverse_lazy('blog_list')

# Update View
class BlogUpdate(UpdateView):
    model = Blog
    form_class = BlogForm
    # Setting returning URL
    success_url = reverse_lazy('blog_list')

# Delete View
class BlogDelete(DeleteView):
    model = Blog
    # Setting returning URL
    success_url = reverse_lazy('blog_list')