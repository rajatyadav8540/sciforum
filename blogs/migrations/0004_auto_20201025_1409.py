# Generated by Django 3.1 on 2020-10-25 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20201024_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='blog_content',
            field=models.TextField(default='', max_length=5000),
        ),
    ]
