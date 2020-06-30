from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=50)
    body = models.TextField(blank=True)
    owner = models.ForeignKey(
        User,
        related_name='todos',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
