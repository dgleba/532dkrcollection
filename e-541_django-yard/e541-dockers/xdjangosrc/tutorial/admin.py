
# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Person


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'place', 'created_at', 'updated_at')
    # list_filter = ('created_at', 'updated_at')
    search_fields = ('name','place',)
    # date_hierarchy = 'created_at'



# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     readonly_fields = ('votes',)
#     extra = 3


# class PollAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {
#             'fields': ['question'],
#         }),
#     ]
#     inlines = [ChoiceInline]
#     list_display = ('question',)
#     search_fields = ['question']

# admin.site.register(Poll, PollAdmin)
# admin.site.register(Choice)

