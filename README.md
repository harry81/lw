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

# 확인

## 환자
```
$ curl http://localhost:8000/stat/patient/ | jq .

{
  "total": 1000,
  "gender": [
    {
      "gender_concept__concept_name": "FEMALE",
      "cnt": 452
    },
    {
      "gender_concept__concept_name": "MALE",
      "cnt": 548
    }
  ],
  "race": [
    {
      "race_source_value": "other",
      "cnt": 1
    },
    {
      "race_source_value": "native",
      "cnt": 3
    },
    {
      "race_source_value": "black",
      "cnt": 86
    },
    {
      "race_source_value": "white",
      "cnt": 845
    },
    {
      "race_source_value": "asian",
      "cnt": 65
    }
  ],
  "ethnicity": [
    {
      "ethnicity_source_value": "nonhispanic",
      "cnt": 880
    },
    {
      "ethnicity_source_value": "hispanic",
      "cnt": 120
    }
  ],
  "death": 152

```

## 방문

```
$ curl http://localhost:8000/stat/visit/ | jq .

{
  "visit_type": [
    {
      "visit_type_concept__concept_name": "Visit derived from encounter on claim",
      "cnt": 41810
    }
  ],
  "gender": [
    {
      "person__gender_concept__concept_name": "FEMALE",
      "cnt": 19307
    },
    {
      "person__gender_concept__concept_name": "MALE",
      "cnt": 22503
    }
  ],
  "race": [
    {
      "person__race_source_value": "other",
      "cnt": 82
    },
    {
      "person__race_source_value": "native",
      "cnt": 89
    },
    {
      "person__race_source_value": "black",
      "cnt": 3326
    },
    {
      "person__race_source_value": "white",
      "cnt": 35487
    },
    {
      "person__race_source_value": "asian",
      "cnt": 2826
    }
  ],
  "ethnicity": [
    {
      "person__ethnicity_source_value": "nonhispanic",
      "cnt": 36981
    },
    {
      "person__ethnicity_source_value": "hispanic",
      "cnt": 4829
    }
  ],
  "age_group": {
    "0": 3282,
    "1": 4884,
    "2": 5515,
    "3": 5631,
    "4": 5970,
    "5": 5865,
    "6": 4576,
    "7": 3606,
    "8": 1594,
    "9": 834,
    "10": 53
  }
}

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



# 궁금증

## person.gender_concept, person.gender_source_value 이유?
