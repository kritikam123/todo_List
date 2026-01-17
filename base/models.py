from django.db import models
from django.contrib.auth.models import User
# Create your models here.Database table in django is represented as a model class which is a subclass of django.db.models.Model. Each attribute of the model represents a database field.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['complete']  # Orders tasks by their completion status
        
