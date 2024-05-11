from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS_CONSTANTS = (
        ('todo','TODO'),
        ('done','DONE'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CONSTANTS, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name