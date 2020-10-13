# Import path to define URL pattern
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('new', views.BlogCreate.as_view(), name='blog_new'),
    path('view/<int:pk>', views.BlogView.as_view(), name='blog_view'),
    path('edit/<int:pk>', views.BlogUpdate.as_view(), name='blog_edit'),
    path('delete/<int:pk>', views.BlogDelete.as_view(), name='blog_delete'),
]