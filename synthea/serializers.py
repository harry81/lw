from rest_framework import serializers

from synthea.models import (Concept, ConditionOccurrence, DrugExposure, Person,
                            VisitOccurrence, Death)


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['concept_id', 'concept_name', 'domain_id', 'vocabulary_id', 'concept_code']


class ConceptSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['concept_id', 'concept_name']


class PersonSerializer(serializers.ModelSerializer):
    gender_concept = ConceptSimpleSerializer(many=False, read_only=True)
    race_concept = ConceptSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = Person
        fields = '__all__'


class VisitOccurrenceSerializer(serializers.ModelSerializer):
    visit_concept = ConceptSimpleSerializer(many=False, read_only=True)
    visit_type_concept = ConceptSimpleSerializer(many=False, read_only=True)
    visit_source_concept = ConceptSimpleSerializer(many=False, read_only=True)
    discharge_to_concept = ConceptSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = VisitOccurrence
        fields = '__all__'


class ConditionOccurrenceSerializer(serializers.ModelSerializer):
    condition_concept = ConceptSimpleSerializer(many=False, read_only=True)
    condition_type_concept = ConceptSimpleSerializer(many=False, read_only=True)
    condition_status_concept = ConceptSimpleSerializer(many=False, read_only=True)
    condition_source_concept = ConceptSimpleSerializer(many=False, read_only=True)

    class Meta:
        model = ConditionOccurrence
        fields = '__all__'


class DrugExposureSerializer(serializers.ModelSerializer):
     drug_concept = ConceptSimpleSerializer(many=False, read_only=True)
     drug_type_concept = ConceptSimpleSerializer(many=False, read_only=True)
     route_concept = ConceptSimpleSerializer(many=False, read_only=True)
     drug_source_concept = ConceptSimpleSerializer(many=False, read_only=True)

     class Meta:
         model = DrugExposure
         fields = '__all__'


class DeathSerializer(serializers.ModelSerializer):
     cause_concept = ConceptSimpleSerializer(many=False, read_only=True)
     cause_source_concept = ConceptSimpleSerializer(many=False, read_only=True)

     class Meta:
         model = Death
         fields = '__all__'
