# Generated by Django 3.1 on 2020-11-13 16:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_remove_event_event_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_content',
            field=ckeditor.fields.RichTextField(default='', max_length=5000),
        ),
    ]
