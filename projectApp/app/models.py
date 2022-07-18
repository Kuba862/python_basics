from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title