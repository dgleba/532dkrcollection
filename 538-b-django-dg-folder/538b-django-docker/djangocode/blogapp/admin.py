from django.contrib import admin
from django import forms

from . import models


class BookAdminForm(forms.ModelForm):

    class Meta:
        model = models.Book
        fields = "__all__"


class BookAdmin(admin.ModelAdmin):
    form = BookAdminForm
    list_display = [
        "created",
        "name",
        "author",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "name",
        "author",
        "last_updated",
    ]


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "body",
        "last_updated",
        "created",
        "title",
    ]
    readonly_fields = [
        "body",
        "last_updated",
        "created",
        "title",
    ]


admin.site.register(models.Book, BookAdmin)
admin.site.register(models.Post, PostAdmin)
