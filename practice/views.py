from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from django.utils.functional import cached_property
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, status, generics, mixins
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet

from practice.models import Student, Issue, Candidate, Vote
from practice.serializers import CandidateSerializer, StudentSerializer, VoteSerializer

"""
def student_list(request):
   
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        serializer = StudentSerializer()
        return JsonResponse(serializer.errors, status=400)


def candidate_list(request):
    if request.method == 'GET':
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates, many=True)
        return JsonResponse(serializer.data, safe=False)

    else:
        serializer = CandidateSerializer()
        return JsonResponse(serializer.errors, status=400)

"""


class CandidateViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Candidate.objects.all().with_vote_counts()
    serializer_class = CandidateSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    search_fields = ["first_name", "last_name"]
    ordering_fields = ["first_name", "last_name", "grade"]
    filterset_fields = ['grade']


class VoteViewSet(mixins.CreateModelMixin, GenericViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer


