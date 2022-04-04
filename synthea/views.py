import collections

from django.db.models import Count, F
from django.db.models.functions import ExtractDay
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from synthea.models import Death, Person, VisitOccurrence


class StatViewSet(viewsets.ViewSet):

    def list(self, request):
        return Response('patient and visit')

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

    @action(detail=False)
    def visit(self, request):
        age_group_temp = collections.Counter(VisitOccurrence.objects.annotate(duration=(F('visit_start_datetime') - F('person__birth_datetime'))).\
                                             annotate(day=ExtractDay('duration')).annotate(age=F('day') / (365 * 10)).values_list('age', flat=True))
        age_group = dict(sorted(age_group_temp.items(), key=lambda item: item[0]))

        res = {
            'visit_type': VisitOccurrence.objects.values('visit_type_concept__concept_name').\
            annotate(cnt=Count('visit_type_concept__concept_name')),
            'gender': VisitOccurrence.objects.values('person__gender_concept__concept_name').\
            annotate(cnt=Count('person__gender_concept__concept_name')),
            'race': VisitOccurrence.objects.values('person__race_source_value').\
            annotate(cnt=Count('person__race_source_value')),
            'ethnicity': VisitOccurrence.objects.values('person__ethnicity_source_value').\
            annotate(cnt=Count('person__ethnicity_source_value')),
            'age_group': age_group
        }
        return Response(res)
