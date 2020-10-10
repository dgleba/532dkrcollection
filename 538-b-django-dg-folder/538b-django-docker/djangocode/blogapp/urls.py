from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("Book", api.BookViewSet)
router.register("Post", api.PostViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("blogapp/Book/", views.BookListView.as_view(), name="blogapp_Book_list"),
    path("blogapp/Book/create/", views.BookCreateView.as_view(), name="blogapp_Book_create"),
    path("blogapp/Book/detail/<int:pk>/", views.BookDetailView.as_view(), name="blogapp_Book_detail"),
    path("blogapp/Book/update/<int:pk>/", views.BookUpdateView.as_view(), name="blogapp_Book_update"),
    path("blogapp/Post/", views.PostListView.as_view(), name="blogapp_Post_list"),
    path("blogapp/Post/create/", views.PostCreateView.as_view(), name="blogapp_Post_create"),
    path("blogapp/Post/detail/<int:pk>/", views.PostDetailView.as_view(), name="blogapp_Post_detail"),
    path("blogapp/Post/update/<int:pk>/", views.PostUpdateView.as_view(), name="blogapp_Post_update"),

    path("select2/", include("django_select2.urls")),
)
