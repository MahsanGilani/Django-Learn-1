from django.db import models
from django.template.defaultfilters import slugify
import random

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateTimeField()
    # slug = models.SlugField(unique=True)
    
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     abc = Todo.objects.values('title')
    #     # for item in abc:
    #     if self.title in abc:
    #         f'{self.title}{random.randint(0,1000000000)}'
    #     super(Todo, self).save(*args, **kwargs)