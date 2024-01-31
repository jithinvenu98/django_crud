from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(verbose_name="Student Name", max_length=100)
    email = models.EmailField(verbose_name="Student Email",max_length=277)

    def __str__(self):
      return str(self.id)
  