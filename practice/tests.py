from django.test import TestCase

# Create your tests here.

from django.urls import reverse, reverse_lazy
from rest_framework import status
from rest_framework.test import APITestCase
from practice.models import Student, Issue, Candidate, CandidateIssue, Vote

class CandidateTests(APITestCase):
    def test_candidate(self):
        """
        Ensure we return the list view
        """
        url = reverse('candidates-list')
        print(url, type(url))
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert Candidate.objects.count()== len(response.json())

    def test_vote_submission(self):
        """
        Ensure we can create a new account object.
        """
        starting_count = Vote.objects.count()
        data = { "candidate":3,
                 "student":2}
        response = self.client.post("/vote/", data, format='json')
        print(response.data)
        assert response.status_code == status.HTTP_201_CREATED
        assert Vote.objects.count() - starting_count == 1
