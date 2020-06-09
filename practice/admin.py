from django.contrib import admin

# Register your models here.
from practice.models import Student, Issue, Candidate, CandidateIssue


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "student_number")

@admin.register(Issue)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "issue_name")

@admin.register(Candidate)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "grade")
    search_fields = ["first_name", "last_name"]
    filterset_fields = ['grade']


@admin.register(CandidateIssue)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("pk", "candidate", "issue", "issue_rank")

