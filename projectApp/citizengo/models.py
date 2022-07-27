from django.db import models
from django.contrib.auth.models import User

# class Topics(models.Model):
#     TOPIC = (
#         ('LF', 'Life'),
#         ('FM', 'Family'),
#         ('PT', 'Politics'),
#         ('SD', 'Solidarity'),
#         ('ED', 'Education'),
#         ('OT', 'Other')
#     )
#     name = models.CharField(max_length=2, choices=TOPIC)
    
#     def __str__(self):
#         return self.name
    
class Creator(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    petition = models.ForeignKey('Petition', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.body[0:50]

class Petition(models.Model):
    TOPIC = (
        ('Life', 'LF'),
        ('Family', 'FM'),
        ('Politics', 'PT'),
        ('Solidarity', 'SD'),
        ('Education', 'ED'),
        ('Other', 'OT')
    )
    title = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    createDate = models.DateTimeField(auto_now_add=True)
    letter = models.CharField(max_length=200)
    topic = models.CharField(max_length=10, choices=TOPIC)
    image = models.ImageField(upload_to='static/images', null=True)
    
    def __str__(self):
        return self.description[0:350]
    
