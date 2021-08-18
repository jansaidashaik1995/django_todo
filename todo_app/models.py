from django.db import models

# Create your models here.
class Todo(models.Model):
    added_date = models.DateField()
    todo = models.CharField(max_length=200)

