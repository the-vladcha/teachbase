from django.contrib.postgres.fields import ArrayField
from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.IntegerField()
    content_type = models.IntegerField()
    owner_name = models.TextField()
    thumb_url = models.URLField()
    cover_url = models.URLField()
    description = models.TextField()
    last_activity = models.DateTimeField(auto_now=True)
    total_score = models.IntegerField()
    total_tasks = models.IntegerField()
    is_netology = models.BooleanField(default=False)
    bg_url = models.URLField()
    video_url = models.URLField(default='')
    demo = models.BooleanField(default=False)
    unchangeable = models.BooleanField(default=False)
    include_weekly_report = models.BooleanField(default=False)
    custom_author_names = models.CharField(max_length=100)
    custom_contents_link = models.CharField(max_length=250)
    hide_viewer_navigation = models.BooleanField(default=False)
    duration = models.IntegerField()
    account_id = models.IntegerField()
    authors = ArrayField(base_field=models.JSONField(), default=list)
    types = ArrayField(base_field=models.JSONField(), default=list)
    sections = ArrayField(base_field=models.JSONField(), default=list)

    def __str__(self):
        return self.name
