from synthea.models import Concept, Person
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
        fields = ['person_id', 'gender_concept', 'race_concept', 'year_of_birth',
                  'month_of_birth', 'day_of_birth', 'birth_datetime', 'gender_source_value', 'race_source_value',
                  'ethnicity_source_value', 'ethnicity_source_concept_id'
                  ]
