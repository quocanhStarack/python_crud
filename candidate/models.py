from django.db import models
from django.core.validators import URLValidator
# Create your models here.


class Candidate(models.Model):
    status = models.IntegerField()
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    dob = models.DateField()
    major = models.CharField(max_length=50)
    work_experience = models.TextField()
    cv = models.URLField(blank=True)

    
    def __str__(self):
        return self.name

    class Meta:
        db_table = "candidate"

