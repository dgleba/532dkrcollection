# Generated by Django 2.2.16 on 2020-10-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
