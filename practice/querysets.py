from django.db.models import QuerySet, Count


class CandidateQuerySet(QuerySet):
    def with_vote_counts(self):
        return self.annotate(vote_count = Count("candidate_votes"))
