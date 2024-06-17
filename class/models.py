from django.db import models

# Create your models here.

class Class(models.Model):
    class_id = models.IntegerField()
    class_name = models.CharField(max_length = 20)
    department = models.CharField(max_length = 20)
    start_date = models.DateField()
    end_date = models.DateField()
    teacher_id = models.IntegerField()
    school_year = models.DateField()
    capacity = models.SmallIntegerField()
    room_number = models.IntegerField()
    grade_level = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

