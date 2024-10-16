from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.CharField(max_length = 12 ,primary_key = True)
    title = models.TextField(max_length = 100)
    author = models.TextField(max_length = 100)
    published_year = models.IntegerField(max_length = 12)

class Student(models.Model):
    student_id = models.CharField(max_length=12,primary_key=True)
    student_name = models.TextField(max_length=100)
    student_phone = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    stud_status = models.CharField(max_length=100,default='active')

class Borrowing(models.Model):
    borrow_id = models.CharField(max_length=100, primary_key=True)
    book_id = models.ForeignKey(Book,on_delete =  models.CASCADE)
    student_id = models.ForeignKey(Student,on_delete  = models.CASCADE)
    borrow_date = models.DateField(max_length=100)
    return_date = models.DateField(max_length=100)

class Course(models.Model) :
    code = models.CharField(max_length=4,primary_key=True)
    description = models.TextField()

class Mentor(models.Model):
    menid = models.CharField(max_length=10,primary_key=True)
    menname = models.TextField(max_length=225)
    menroomno = models.CharField(max_length=3,default='sk2')