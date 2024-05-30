from django.db import models
from author.models import author

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length=20)
    about = models.TextField()
    authors = models.OneToOneField(author, on_delete=models.CASCADE , default=None)
    
    def __str__(self):
        return self.name
       
    