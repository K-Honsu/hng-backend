from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=1000, unique=True)
    
    def __str__(self) -> str:
        return f"Person's name is {self.name}"