from django.db.models import Count
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from synthea.models import Death, Person


class StatViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response('')

    @action(detail=False)
    def patient(self, request):
        res = {
            'total': Person.objects.count(),
            'gender': Person.objects.values('gender_concept__concept_name').annotate(cnt=Count('gender_concept')),
            'race': Person.objects.values('race_source_value').annotate(cnt=Count('race_source_value')),
            'ethnicity': Person.objects.values('ethnicity_source_value').annotate(cnt=Count('ethnicity_source_value')),
            'death': Death.objects.count()
        }
        return Response(res)
