from django.contrib import admin
from.models import Course,Student,Borrowing,Book,Mentor 

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    pass

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass

@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    pass

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass

@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    pass

# Register your models here.
