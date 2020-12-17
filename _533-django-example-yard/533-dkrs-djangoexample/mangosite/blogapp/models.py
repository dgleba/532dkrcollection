from django.db import models
from django.urls import reverse

from django.conf import settings
from django.db import models
import rules


class Post(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    title = models.CharField(max_length=230)
    body = models.TextField(max_length=32100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("blogapp_Post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("blogapp_Post_update", args=(self.pk,))

if sys.version_info.major >= 3:
    from rules.contrib.models import RulesModel

    class TestModel(RulesModel):
        class Meta:
            rules_permissions = {"add": rules.always_true, "view": rules.always_true}

        @classmethod
        def preprocess_rules_permissions(cls, perms):
            perms["custom"] = rules.always_true
