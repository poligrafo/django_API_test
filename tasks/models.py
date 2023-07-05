from django.db import models


class New_task(models.Model):
    app_label = 'tasks'
    title = models.CharField(max_length=255)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
