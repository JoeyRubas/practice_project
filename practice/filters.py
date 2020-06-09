from django_filters import rest_framework as filters

from practice.models import Candidate


class CandidateFilter(filters.FilterSet):
    top_issue = filters.CharFilter(method=filter_top_issue)
    class Meta:
        model = Candidate
    def filter_top_issue(self, qs, name, value):
        if value:
            qs.filter(candidate_issues__issue_id__in=value)
