from django.contrib import admin
from django import forms

from . import models


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "created",
        "last_updated",
        "title",
        "body",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "title",
        "body",
    ]


admin.site.register(models.Post, PostAdmin)
