from django.http.response import Http404, HttpResponse, HttpResponseNotAllowed, HttpResponseNotFound
from django.shortcuts import render
from django.http import Http404
from django.contrib.auth.models import User
from .models import AbsenceType, Student, Grade
# Create your views here.
def index(response):
    students_class_wise= {}
    for i in range(6,12):
        students_class_wise[i]=(Student.objects.filter(grade=Grade.objects.get(grade=i)).order_by("f_name"))
    return render(response, "main/home.html", {
        "classes": range(6,12),
        "students": students_class_wise,
        "user": response.user,
    })

def studentDetails(response, id):
    student= Student.objects.get(id=id)
    presences= student.personal_logs.filter(is_present=True)
    informed= student.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Informed"))
    uninformed= student.personal_logs.filter(is_present=False, AbsenceType=AbsenceType.objects.get(type="Uninformed"))
    return render(response, "main/studentDetails.html", {
        "student":student,
        "presences": presences.order_by("date").reverse(),
        "informed":informed.order_by("date").reverse(),
        "uninformed":uninformed.order_by("date").reverse(),
        "user": response.user,
    })

def error_404_view(response, exception):
    return render(response, "main/404.html",{} )