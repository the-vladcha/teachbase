# Generated by Django 4.2 on 2023-04-10 18:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner_id', models.IntegerField()),
                ('content_type', models.IntegerField()),
                ('owner_name', models.TextField()),
                ('thumb_url', models.URLField()),
                ('cover_url', models.URLField()),
                ('description', models.TextField()),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('total_score', models.IntegerField()),
                ('total_tasks', models.IntegerField()),
                ('is_netology', models.BooleanField(default=False)),
                ('bg_url', models.URLField()),
                ('video_url', models.URLField(default='')),
                ('demo', models.BooleanField(default=False)),
                ('unchangeable', models.BooleanField(default=False)),
                ('include_weekly_report', models.BooleanField(default=False)),
                ('custom_author_names', models.CharField(max_length=100)),
                ('custom_contents_link', models.CharField(max_length=250)),
                ('hide_viewer_navigation', models.BooleanField(default=False)),
                ('duration', models.IntegerField()),
                ('account_id', models.IntegerField()),
                ('authors', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None)),
                ('types', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None)),
                ('sections', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), default=list, size=None)),
            ],
        ),
    ]