# Generated by Django 2.2.16 on 2020-10-12 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]