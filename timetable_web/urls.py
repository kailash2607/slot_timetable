from django.urls import path
from . import views

urlpatterns = [
    path('', views.timetable_page, name='timetable'),
]
