from django.db import models

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)
