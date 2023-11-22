from django.contrib import admin
from .models import Student, Department, Professor, Course, Enrollment, Classroom, Schedule, Assignment

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Professor)
admin.site.register(Course)
admin.site.register(Enrollment)
admin.site.register(Classroom)
admin.site.register(Schedule)
admin.site.register(Assignment)