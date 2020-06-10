from django.core.management.base import BaseCommand, CommandError
from practice.models import Issue, Candidate, CandidateIssue

class Command(BaseCommand):
    def handle(self, *args, **options):
        for num in range(5):
            Issue.objects.get_or_create(issue_name=f"issue {num}")


        candidate1, _ = Candidate.objects.get_or_create(first_name="John", last_name="Doe", grade="10th")
        candidate2, _ = Candidate.objects.get_or_create(first_name="Jane", last_name="Doe", grade="10th")

        issue_relationship1 = CandidateIssue.objects.get_or_create(candidate=candidate1, issue=Issue.objects.get(issue_name="issue 1"), issue_rank=1)
        issue_relationship2 = CandidateIssue.objects.get_or_create(candidate=candidate1, issue=Issue.objects.get(issue_name="issue 2"), issue_rank=2)
        issue_relationship3 = CandidateIssue.objects.get_or_create(candidate=candidate2, issue=Issue.objects.get(issue_name="issue 3"), issue_rank=1)
        issue_relationship4 = CandidateIssue.objects.get_or_create(candidate=candidate2, issue=Issue.objects.get(issue_name="issue 4"), issue_rank=2)





