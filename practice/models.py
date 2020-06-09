from django.db import models

# Create your models here.



class Issue(models.Model):
    issue_name = models.CharField(max_length=50)


class Candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    GRADES = [
    ('9th', 'Freshman'),
    ('10th', 'Sophomore'),
    ('11th', 'Junior'),
    ('12th', 'Senior')]
    grade = models.CharField(max_length=50, choices=GRADES)

class Student(models.Model):
    student_number = models.IntegerField()
    vote = models.ForeignKey(Candidate, on_delete=models.CASCADE, blank=True, null=True)

class CandidateIssue(models.Model):
    candidate = models.ForeignKey(Candidate, related_name="candidate_issues" ,on_delete=models.CASCADE, blank = True)
    issue = models.ForeignKey(Issue, related_name="candidates", on_delete=models.CASCADE, blank = True)
    issue_rank = models.IntegerField()


