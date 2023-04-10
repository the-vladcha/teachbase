from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner_id = models.IntegerField(blank=True)
    content_type = models.IntegerField(blank=True)
    owner_name = models.TextField(blank=True)
    thumb_url = models.URLField(blank=True)
    cover_url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    last_activity = models.DateTimeField(auto_now=True)
    total_score = models.IntegerField(blank=True)
    total_tasks = models.IntegerField(blank=True)
    is_netology = models.BooleanField(default=False)
    bg_url = models.URLField(blank=True)
    video_url = models.URLField(default='', blank=True)
    demo = models.BooleanField(default=False)
    unchangeable = models.BooleanField(default=False)
    include_weekly_report = models.BooleanField(default=False)
    custom_author_names = models.CharField(max_length=100, blank=True)
    custom_contents_link = models.CharField(max_length=250, blank=True)
    hide_viewer_navigation = models.BooleanField(default=False)
    duration = models.IntegerField(blank=True, null=True)
    account_id = models.IntegerField(blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name
