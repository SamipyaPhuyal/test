from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=25)
    grade=models.IntegerField(default=11)
    stream=models.CharField(default="science")
    
    def __str__(self):
        return self.name