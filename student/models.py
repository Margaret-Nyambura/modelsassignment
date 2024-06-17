from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    email = models.EmailField()
    date_of_birth = models.DateField()
    code = models.PositiveSmallIntegerField()
    country = models.CharField(max_length = 28)
    gender = models.CharField(max_length = 6)
    bio = models.TextField()
    id_number = models.IntegerField()
    grade_level = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
