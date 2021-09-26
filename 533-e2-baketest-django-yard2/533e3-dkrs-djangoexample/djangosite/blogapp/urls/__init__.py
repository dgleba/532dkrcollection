from django.conf.urls import include, url

app_name="blogapp"

urlpatterns = [

    url(r'^posts/', include('blogapp.urls.post_urls')),  # NOQA
    url(r'^authors/', include('blogapp.urls.author_urls')),
    url(r'^books/', include('blogapp.urls.book_urls')),
    url(r'^persons/', include('blogapp.urls.person_urls')),
    url(r'^groups/', include('blogapp.urls.group_urls')),
]
