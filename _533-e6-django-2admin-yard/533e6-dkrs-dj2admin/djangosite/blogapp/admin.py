from django.contrib import admin
from django import forms

from . import models

from django.utils.html import format_html
# old.. from django.core.urlresolvers import reverse
from django.urls import reverse


from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse

# from .forms import DepositForm, WithdrawForm


# =================================================
# =================================================



# first admin site



class PostAdminForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    # add_form_template = 'blogapp/admin/postadd.html'
    form = PostAdminForm
    list_display = [
        # "id",
        # "created",
        # "last_updated",
        "title",
        "body",
    ]

admin.site.register(models.Post, PostAdmin)


# =================================================


# second admin site



class PostAdmin2(admin.AdminSite):
    site_header = "Blog Post"
    site_title = "Posts"
    index_title = "Welcome to dgammyblog"

class PostAdmin2Model(admin.ModelAdmin):
    add_form_template = 'blogapp/admin/postadd.html'
    form = PostAdminForm
    list_display = [
        "title",
        "id",
        "created",
        "last_updated",
        "body",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
        # "title",
        # "body",
    ]


post_admin2 = PostAdmin2(name='post_admin')

post_admin2.register(models.Post, PostAdmin2Model)


# =================================================

# =================================================

