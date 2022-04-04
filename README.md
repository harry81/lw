# 설정

## DB 접속
```
export DB_NAME="synthe~"
export DB_USER="walke~"
export DB_PW="******"
export DB_HOST="localhost"
```

# 실행

```
$ python manage.py runserver
```


# troubleshooting

## 이미 존재하는 db schema를 django models 로 인식 시키디

```
$ python manage.py inspectdb
```

## Reverse accessor는 수작업으로 처리
```
ERRORS:
synthea.ConditionOccurrence.condition_source_concept: (fields.E304) Reverse accessor for 'synthea.ConditionOccurrence.condition_source_concept' clashes with reverse accessor for 'synthea.ConditionOccurrence.condition_status_concept'.
        HINT: Add or change a related_name argument to the definition for 'synthea.ConditionOccurrence.condition_source_concept' or 'synthea.ConditionOccurrence.condition_status_concept'.
synthea.ConditionOccurrence.condition_source_concept: (fields.E304) Reverse accessor for 'synthea.ConditionOccurrence.condition_source_concept' clashes with reverse accessor for 'synthea.ConditionOccurrence.condition_type_concept'.
        HINT: Add or change a related_name argument to the definition for 'synthea.ConditionOccurrence.condition_source_concept' or 'synthea.ConditionOccurrence.condition_type_concept'.
synthea.ConditionOccurrence.condition_status_concept: (fields.E304) Reverse accessor for 'synthea.ConditionOccurrence.condition_status_concept' clashes with reverse accessor for 'synthea.ConditionOccurrence.condition_source_concept'.
        HINT: Add or change a related_name argument to the definition for 'synthea.ConditionOccurrence.condition_status_concept' or 'synthea.ConditionOccurrence.condition_source_concept'.
```
