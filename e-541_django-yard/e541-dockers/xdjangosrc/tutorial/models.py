# tutorial/models.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# import django.urls to set absolute URL
from django.urls import reverse
from django.conf import settings
from django.db import models

import django_filters

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="full_name")
    place = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
