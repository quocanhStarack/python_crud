from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,default='')
    description = models.TextField()
    author = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'posts'