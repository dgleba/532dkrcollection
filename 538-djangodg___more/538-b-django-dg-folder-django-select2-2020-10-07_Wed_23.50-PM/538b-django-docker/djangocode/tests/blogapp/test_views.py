import pytest
import test_helpers

from django.urls import reverse
from django.test import Client


pytestmark = [pytest.mark.django_db]


def tests_Book_list_view():
    instance1 = test_helpers.create_blogapp_Book()
    instance2 = test_helpers.create_blogapp_Book()
    client = Client()
    url = reverse("blogapp_Book_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Book_create_view():
    client = Client()
    url = reverse("blogapp_Book_create")
    data = {
        "name": "text",
        "author": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Book_detail_view():
    client = Client()
    instance = test_helpers.create_blogapp_Book()
    url = reverse("blogapp_Book_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Book_update_view():
    client = Client()
    instance = test_helpers.create_blogapp_Book()
    url = reverse("blogapp_Book_update", args=[instance.pk, ])
    data = {
        "name": "text",
        "author": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Post_list_view():
    instance1 = test_helpers.create_blogapp_Post()
    instance2 = test_helpers.create_blogapp_Post()
    client = Client()
    url = reverse("blogapp_Post_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Post_create_view():
    Book = test_helpers.create_blogapp_Book()
    client = Client()
    url = reverse("blogapp_Post_create")
    data = {
        "body": "text",
        "title": "text",
        "Book": Book.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Post_detail_view():
    client = Client()
    instance = test_helpers.create_blogapp_Post()
    url = reverse("blogapp_Post_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Post_update_view():
    Book = test_helpers.create_blogapp_Book()
    client = Client()
    instance = test_helpers.create_blogapp_Post()
    url = reverse("blogapp_Post_update", args=[instance.pk, ])
    data = {
        "body": "text",
        "title": "text",
        "Book": Book.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
