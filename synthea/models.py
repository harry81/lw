# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'



class Concept(models.Model):
    concept_id = models.IntegerField(primary_key=True)
    concept_name = models.CharField(max_length=255, blank=True, null=True)
    domain_id = models.CharField(max_length=20, blank=True, null=True)
    vocabulary_id = models.CharField(max_length=20, blank=True, null=True)
    concept_class_id = models.CharField(max_length=20, blank=True, null=True)
    standard_concept = models.CharField(max_length=1, blank=True, null=True)
    concept_code = models.CharField(max_length=50, blank=True, null=True)
    valid_start_date = models.DateField(blank=True, null=True)
    valid_end_date = models.DateField(blank=True, null=True)
    invalid_reason = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'concept'


class Person(models.Model):
    person_id = models.BigIntegerField(primary_key=True)
    gender_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='person_gender_concept')
    year_of_birth = models.IntegerField(blank=True, null=True)
    month_of_birth = models.IntegerField(blank=True, null=True)
    day_of_birth = models.IntegerField(blank=True, null=True)
    birth_datetime = models.DateTimeField(blank=True, null=True)
    race_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    ethnicity_concept_id = models.IntegerField(blank=True, null=True)
    location_id = models.BigIntegerField(blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    person_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_value = models.CharField(max_length=50, blank=True, null=True)
    gender_source_concept_id = models.IntegerField(blank=True, null=True)
    race_source_value = models.CharField(max_length=50, blank=True, null=True)
    race_source_concept_id = models.IntegerField(blank=True, null=True)
    ethnicity_source_value = models.CharField(max_length=50, blank=True, null=True)
    ethnicity_source_concept_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person'


class ConditionOccurrence(models.Model):
    condition_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    condition_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='co_concept')
    condition_start_date = models.DateField(blank=True, null=True)
    condition_start_datetime = models.DateTimeField(blank=True, null=True)
    condition_end_date = models.DateField(blank=True, null=True)
    condition_end_datetime = models.DateTimeField(blank=True, null=True)
    condition_type_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='co_type_concept')
    condition_status_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.DO_NOTHING, blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    condition_source_value = models.CharField(max_length=50, blank=True, null=True)
    condition_source_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='co_source_concept')
    condition_status_source_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'condition_occurrence'


class Death(models.Model):
    person = models.OneToOneField('Person', models.DO_NOTHING, primary_key=True)
    death_date = models.DateField(blank=True, null=True)
    death_datetime = models.DateTimeField(blank=True, null=True)
    death_type_concept_id = models.IntegerField(blank=True, null=True)
    cause_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='death_co')
    cause_source_value = models.IntegerField(blank=True, null=True)
    cause_source_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'death'


class DrugExposure(models.Model):
    drug_exposure_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey('Person', models.DO_NOTHING, blank=True, null=True)
    drug_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='de_drug_concept')
    drug_exposure_start_date = models.DateField(blank=True, null=True)
    drug_exposure_start_datetime = models.DateTimeField(blank=True, null=True)
    drug_exposure_end_date = models.DateField(blank=True, null=True)
    drug_exposure_end_datetime = models.DateTimeField(blank=True, null=True)
    verbatim_end_date = models.DateField(blank=True, null=True)
    drug_type_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='de_drug_type_concept')
    stop_reason = models.CharField(max_length=20, blank=True, null=True)
    refills = models.IntegerField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=10, blank=True, null=True)
    days_supply = models.IntegerField(blank=True, null=True)
    sig = models.TextField(blank=True, null=True)
    route_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='de_route_concept')
    lot_number = models.CharField(max_length=50, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    visit_occurrence = models.ForeignKey('VisitOccurrence', models.DO_NOTHING, blank=True, null=True)
    visit_detail_id = models.BigIntegerField(blank=True, null=True)
    drug_source_value = models.CharField(max_length=50, blank=True, null=True)
    drug_source_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    route_source_value = models.CharField(max_length=50, blank=True, null=True)
    dose_unit_source_value = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_exposure'



class VisitOccurrence(models.Model):
    visit_occurrence_id = models.BigIntegerField(primary_key=True)
    person = models.ForeignKey(Person, models.DO_NOTHING, blank=True, null=True)
    visit_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='vo_concept')
    visit_start_date = models.DateField(blank=True, null=True)
    visit_start_datetime = models.DateTimeField(blank=True, null=True)
    visit_end_date = models.DateField(blank=True, null=True)
    visit_end_datetime = models.DateTimeField(blank=True, null=True)
    visit_type_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True)
    provider_id = models.BigIntegerField(blank=True, null=True)
    care_site_id = models.BigIntegerField(blank=True, null=True)
    visit_source_value = models.CharField(max_length=50, blank=True, null=True)
    visit_source_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='vo_visit_source_concept')
    admitted_from_concept_id = models.IntegerField(blank=True, null=True)
    admitted_from_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_source_value = models.CharField(max_length=50, blank=True, null=True)
    discharge_to_concept = models.ForeignKey(Concept, models.DO_NOTHING, blank=True, null=True, related_name='vo_discharge_to_concept')
    preceding_visit_occurrence = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'visit_occurrence'
