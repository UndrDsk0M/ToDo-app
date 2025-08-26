from django.db import models
from django.contrib.auth.models import User 


class Todo(models.Model):
    name = models.CharField(max_length=50)  

    parent = models.ForeignKey(
        'self',   
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='subtasks'
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        # maybe in updates we'll add date 
        super(Todo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
