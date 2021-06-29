from django.urls import path
from .views import *
urlpatterns=[
    path("log/", attendenceView),
    path("tutor-log/", myLogView)
]
