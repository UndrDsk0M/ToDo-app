from django.db import models
from django.contrib.auth.models import User 


class Todo(models.Model):
    name = models.CharField(max_length=50)  
    description = models.CharField(max_length=500, blank=True, null=True)  

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model

    def save(self, *args, **kwargs):
        # maybe in updates we'll add date 
        super(Todo, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
