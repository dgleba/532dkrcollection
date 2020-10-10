from django.urls import path

from . import views


urlpatterns = [
    path("", views.ThingList.as_view(), name="list"),
    path("new/", views.ThingCreate.as_view(), name="create"),
    path("<int:pk>/", views.ThingDetail.as_view(), name="detail"),
    path("<int:pk>/update/", views.ThingUpdate.as_view(), name="update"),
    path("<int:pk>/delete/", views.ThingDelete.as_view(), name="delete"),
]


app_name = "things"
