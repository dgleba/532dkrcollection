from django.conf.urls import url
from ..views import (GroupListView, GroupCreateView, GroupDetailView,
                     GroupUpdateView, GroupDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(GroupCreateView.as_view()),
        name="group_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(GroupUpdateView.as_view()),
        name="group_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(GroupDeleteView.as_view()),
        name="group_delete"),

    url(r'^(?P<pk>\d+)/$',
        GroupDetailView.as_view(),
        name="group_detail"),

    url(r'^$',
        GroupListView.as_view(),
        name="group_list"),
]
