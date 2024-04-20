from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # Assuming the array contains related items, using a ManyToManyField
    chapters = models.JSONField('self', blank=True, default=dict)
    source_file = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title