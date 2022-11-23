from django.db import models

# Create your models here.

class Todo(models.Model):
    Title = models.CharField(max_length=150, blank=False)
    Date = models.DateTimeField(blank=True)
    is_completed = models.BooleanField(default=False)
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.Title
