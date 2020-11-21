"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
# Setting static files
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView 


# tutorial/views.py
from tutorial.views import *
# PersonListView

# from polls import views
from blog import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    # for select2
    path("blog/create", views.BlogCreate.as_view(), name="blog-create"),
    path("select2/", include("django_select2.urls")),

    path('admin/', admin.site.urls),
    # url(r'^admin/', admin.site.urls),

    # Make Book App as Root
    # url(r'^', include('book.urls')),

    # path('book1/', include('book1.urls')),

    path('book/', include('book.urls')),
    
    path('blog/', include('blog.urls')),

    path('book-app/', include('book-app.urls')),
    
    path("people/", FilteredPersonListView.as_view()),

    # https://learndjango.com/tutorials/hello-world-5-different-ways
    path('', TemplateView.as_view(template_name='blog/home.html'), name='home'), 

    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
