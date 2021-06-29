from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
import datetime
# Create your models here.

class Grade(models.Model):
    grade= models.IntegerField()
    
    def __str__(self):
        return f"{self.grade}"


class Board(models.Model):
    board= models.CharField(max_length=10)

    def __str__(self):
        return f"{self.board}"


class Student(models.Model):
    f_name= models.CharField(max_length=30)
    l_name= models.CharField(max_length=30)
    grade= models.ForeignKey(Grade, on_delete=models.CASCADE)
    board= models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.f_name} {self.l_name} ({self.grade} {self.board})"

    def num_present(self):
        return len(self.personal_logs.filter(is_present=True))
    
    def num_absent_informed(self):
        return len(self.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Informed")))
    
    def num_absent_uninformed(self):
        return len(self.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Uninformed")))
    
    def num_absent_total(self):
        return len(self.personal_logs.filter(is_present=False))



class AbsenceType(models.Model):
    type= models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Log(models.Model):
    TIME_CHOICES= (
        (datetime.time(14,0,0), "2PM"), 
        (datetime.time(15,0,0), "3PM"),
        (datetime.time(16,0,0), "4PM"),
        (datetime.time(17,0,0), "5PM"),
        (datetime.time(18,0,0), "6PM"),
    )
    tutor= models.ForeignKey(User, on_delete=models.CASCADE)
    student= models.ForeignKey(Student, on_delete=models.CASCADE, related_name="personal_logs")
    date= models.DateField()
    time= models.TimeField(choices=TIME_CHOICES)
    is_present=models.BooleanField(default=True)
    AbsenceType=models.ForeignKey(AbsenceType, on_delete=models.CASCADE)

    def logIt(self, tutor, student, date, time, is_present, AbsenceType):
        self.tutor= tutor
        self.student= student
        self.date= date
        self.time= time
        self.is_present= is_present
        self.AbsenceType=AbsenceType

    def __str__(self):
        return f"({self.tutor.first_name}) : {self.student} on {self.date} at {self.time}"