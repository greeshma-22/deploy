from django.db import models
from django.urls import reverse

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("student_app:detail",kwargs={'pk':self.pk})

class Student(models.Model):
    studentName=models.CharField(max_length=256)
    stuentRegisterNo=models.IntegerField()
    studentPhoneNo=models.IntegerField()
    studentStandard=models.IntegerField()
    school = models.ForeignKey(School,related_name='students',on_delete = models.CASCADE )

    def __str__(self):
        return self.studentName

    def get_absolute_url(self):
        return reverse("student_app:detail",kwargs={'pk':self.pk})
