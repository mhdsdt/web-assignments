from django.db import models


class Student(models.Model):
    MAJOR_CHOICES = (
        ('CE', 'Computer Engineering'), ('CS', 'Computer Science'),
        ('EE', 'Electrical Engineering'), ('MSE', 'Material Science Engineering'),
        ('AE', 'Aerospace Engineering'), ('ME', 'Mechanical Engineering'),
        ('CHE', 'Chemical Engineering'), ('IE', 'Industrial Engineering'),
        ('AM', 'Applied Mathematics'), ('P', 'Physics'), ('E', 'Economics')
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_number = models.CharField(max_length=20, unique=True)
    major = models.CharField(max_length=20, choices=MAJOR_CHOICES)
    enrollment_year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.student_number}"


class Department(models.Model):
    DEPARTMENT_CHOICES = (
        ('CE', 'Computer Engineering'), ('EE', 'Electrical Engineering'),
        ('MSE', 'Material Science Engineering'), ('AE', 'Aerospace Engineering'),
        ('ME', 'Mechanical Engineering'), ('CHE', 'Chemical Engineering'),
        ('IE', 'Industrial Engineering'), ('MS', 'Mathematical Science'),
        ('P', 'Physics'), ('E', 'Economics')
    )
    name = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES)
    head_of_department = models.ForeignKey('Professor', on_delete=models.SET_NULL, null=True,
                                           blank=True, related_name='department_head')

    def __str__(self):
        return self.name


class Professor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    staff_number = models.CharField(max_length=20, unique=True)
    hiring_date = models.DateField()
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.staff_number}"


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=20, unique=True)
    unit_count = models.PositiveIntegerField()
    offered_by = models.ForeignKey('Professor', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_name} ({self.course_code}-{self.unit_count})"


class Enrollment(models.Model):
    SEMESTER_CHOICES = [('Spring', 'Spring'), ('Fall', 'Fall')]
    enrolled_student = models.ForeignKey('Student', on_delete=models.CASCADE)
    enrolled_course = models.ForeignKey('Course', on_delete=models.CASCADE)
    semester = models.CharField(max_length=20, choices=SEMESTER_CHOICES)

    def __str__(self):
        return f"{self.enrolled_student} - {self.enrolled_course} ({self.semester})"


class Classroom(models.Model):
    building = models.CharField(max_length=30)
    class_number = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    projector_available = models.BooleanField(default=False)
    whiteboard_available = models.BooleanField(default=True)
    wheelchair_accessible = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.building} - Room {self.class_number}"


class Schedule(models.Model):
    DAY_OF_WEEK_CHOICES = (
        ('Saturday', 'Saturday'), ('Sunday', 'Sunday'), ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
    )
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=DAY_OF_WEEK_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.ForeignKey('Classroom', on_delete=models.SET_NULL)

    def get_day_of_week_display(self):
        return f"On {self.day_of_week.capitalize()}"

    def __str__(self):
        return f"{self.course} | {self.professor} | {self.get_day_of_week_display()} | " \
               f"{self.start_time}-{self.end_time}"


class Assignment(models.Model):
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    number_of_assignment = models.PositiveIntegerField()
    topic = models.CharField(max_length=30)
    deadline = models.DateTimeField()

    def get_ordinal_number_of_assignment(self):
        if self.number_of_assignment % 10 == 1:
            return f"{self.number_of_assignment}st"
        elif self.number_of_assignment % 10 == 2:
            return f"{self.number_of_assignment}nd"
        elif self.number_of_assignment % 10 == 3:
            return f"{self.number_of_assignment}rd"
        else:
            return f"{self.number_of_assignment}th"

    def __str__(self):
        return f"{self.get_ordinal_number_of_assignment()} Assignment from {self.course} Course, " \
               f"with topic of {self.topic} and deadline of {self.deadline}"
