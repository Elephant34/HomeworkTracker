from django.conf import settings
from django.db import models
from django.utils import timezone


class Homework(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False)
    subject = models.CharField(max_length=200)
    task = models.TextField()
    due_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.subject + str(self.due_date)
