from synthea.models import Concept, Person, VisitOccurrence
from rest_framework import serializers



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
