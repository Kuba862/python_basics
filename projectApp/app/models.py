from django.db import models

class MyModel(models.Model):
    title = models.CharField(("Welcome text"), max_length=50)
    description = models.TextField()    
    def __str__(self):
        return self.title
    