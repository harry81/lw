from synthea.models import Concept
from rest_framework import serializers



class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ['concept_id', 'concept_name', 'domain_id', 'vocabulary_id', 'concept_code']
