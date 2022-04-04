import collections

from django.db.models import Count, F
from django.db.models.functions import ExtractDay
from django.shortcuts import render
from rest_framework import filters, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from synthea.models import (Concept, ConditionOccurrence, Death, Person,
                            VisitOccurrence, DrugExposure)
from synthea.serializers import (ConceptSerializer,
                                 ConditionOccurrenceSerializer,
                                 PersonSerializer, VisitOccurrenceSerializer, DrugExposureSerializer, DeathSerializer)


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


class ConceptViewSet(viewsets.ModelViewSet):
    queryset = Concept.objects.all()
    serializer_class = ConceptSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['concept_name',]


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['gender_concept__concept_name', 'year_of_birth', 'ethnicity_source_value']


class VisitOccurrenceViewSet(viewsets.ModelViewSet):
    queryset = VisitOccurrence.objects.all()
    serializer_class = VisitOccurrenceSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['visit_concept__concept_name', 'visit_type_concept__concept_name',
                     'visit_source_concept__concept_name', 'discharge_to_concept__concept_name']


class ConditionOccurrenceViewSet(viewsets.ModelViewSet):
    queryset = ConditionOccurrence.objects.all()
    serializer_class = ConditionOccurrenceSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['condition_concept__concept_name', 'condition_type_concept__concept_name',
                     'condition_status_concept__concept_name', 'condition_source_concept__concept_name']


class DrugExposureViewSet(viewsets.ModelViewSet):
    queryset = DrugExposure.objects.all()
    serializer_class = DrugExposureSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['drug_concept__concept_name', 'drug_type_concept__concept_name',
                     'route_concept__concept_name', 'drug_source_concept__concept_name']


class DeathViewSet(viewsets.ModelViewSet):
    queryset = Death.objects.all()
    serializer_class = DeathSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['cause_concept__concept_name', 'cause_source_concept__concept_name']
