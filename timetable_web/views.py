from django.shortcuts import render

def timetable_page(request):
    return render(request, 'timetable_web/timetable.html')
