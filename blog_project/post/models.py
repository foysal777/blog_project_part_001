from django.db import models
from categories.models import category_model
from author.models import author
# Create your models here.
class post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    categorys = models.ManyToManyField(category_model)
    authors = models.ForeignKey(author,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    