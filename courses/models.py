from django.db import models

# Create your models here.

class Courses(models.Model):
    course_name = models.CharField(max_length = 20)
    course_id = models.IntegerField()
    department = models.CharField(max_length = 20)
    no_of_students = models.IntegerField()
    description = models.CharField(max_length = 28)
    class_name = models.CharField(max_length = 20)
    class_id = models.IntegerField()
    creation_date = models.IntegerField()
    teacher_name = models.CharField(max_length = 25)
    teacher_id = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
