from rest_framework import serializers
from practice.models import Student, Issue, Candidate, CandidateIssue



class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ["student_number", "vote"]

    def update(self, instance, validated_data):
        # Update the Foo instance
        instance.title = validated_data['vote']
        instance.save()
        return instance

class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ["issue_name"]


class CandidateIssueSerializer(serializers.ModelSerializer):
    issue = IssueSerializer()
    class Meta:
        model = CandidateIssue
        fields = ["issue", "issue_rank"]

class CandidateSerializer(serializers.ModelSerializer):
    candidate_issues = CandidateIssueSerializer(many=True)
    class Meta:
        model = Candidate
        fields = ["first_name", "last_name", "grade", "candidate_issues"]

