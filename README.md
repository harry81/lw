# 설정

## DB 접속

아래 환경 변수 값을 shell에 적용합니다.

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

## exam_1 
### 환자
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

### 방문

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

## exam_2

### concept_id들의 정보를 얻을 수 있는 API

```
$ curl http://localhost:8000/concept/\?search\=gender | jq .

{
  "count": 248,
  "next": "http://localhost:8000/concept/?limit=5&offset=5&search=gender",
  "previous": null,
  "results": [
    {
      "concept_id": 45766034,
      "concept_name": "Masculine gender",
      "domain_id": "Gender",
      "vocabulary_id": "SNOMED",
      "concept_code": "703117000"
    },
    {
      "concept_id": 45766035,
      "concept_name": "Feminine gender",
      "domain_id": "Gender",
      "vocabulary_id": "SNOMED",
      "concept_code": "703118005"
    },
    {
      "concept_id": 45774366,
      "concept_name": "[V] Gender dysphoria",
      "domain_id": "Condition",
      "vocabulary_id": "Read",
      "concept_code": "ZV62A00"
    },
    {
      "concept_id": 45883294,
      "concept_name": "Your gender",
      "domain_id": "Meas Value",
      "vocabulary_id": "LOINC",
      "concept_code": "LA15575-6"
    },
    {
      "concept_id": 45888206,
      "concept_name": "Initial comprehensive preventive medicine evaluation and management of an individual including an age and gender appropriate history, examination, counseling/anticipatory guidance/risk factor reduction interventions, and the ordering of laboratory/diagnos",
      "domain_id": "Procedure",
      "vocabulary_id": "CPT4",
      "concept_code": "1013831"
    }
  ]
}

```

## exam_3

각 테이블의 row를 조회하는 API

### person

```
$ curl http://localhost:8000/person/\?search\=hispanic | jq .

{
  "count": 1000,
  "next": "http://localhost:8000/person/?limit=5&offset=5&search=hispanic",
  "previous": null,
  "results": [
    {
      "person_id": 277792,
      "gender_concept": {
        "concept_id": 8507,
        "concept_name": "MALE"
      },
      "race_concept": {
        "concept_id": 8527,
        "concept_name": "White"
      },
      "year_of_birth": 1954,
      "month_of_birth": 4,
      "day_of_birth": 17,
      "birth_datetime": "1954-04-17T00:00:00Z",
      "gender_source_value": "M",
      "race_source_value": "white",
      "ethnicity_source_value": "nonhispanic",
      "ethnicity_source_concept_id": 0
    },
    {
      "person_id": 1022983,
      "gender_concept": {
        "concept_id": 8507,
        "concept_name": "MALE"
      },
      "race_concept": {
        "concept_id": 8527,
        "concept_name": "White"
      },
      "year_of_birth": 1950,
      "month_of_birth": 2,
      "day_of_birth": 26,
      "birth_datetime": "1950-02-26T00:00:00Z",
      "gender_source_value": "M",
      "race_source_value": "white",
      "ethnicity_source_value": "hispanic",
      "ethnicity_source_concept_id": 0
    },
    {
      "person_id": 1786297,
      "gender_concept": {
        "concept_id": 8507,
        "concept_name": "MALE"
      },
      "race_concept": {
        "concept_id": 8527,
        "concept_name": "White"
      },
      "year_of_birth": 1973,
      "month_of_birth": 5,
      "day_of_birth": 29,
      "birth_datetime": "1973-05-29T00:00:00Z",
      "gender_source_value": "M",
      "race_source_value": "white",
      "ethnicity_source_value": "nonhispanic",
      "ethnicity_source_concept_id": 0
    },
    {
      "person_id": 1771720,
      "gender_concept": {
        "concept_id": 8507,
        "concept_name": "MALE"
      },
      "race_concept": {
        "concept_id": 8527,
        "concept_name": "White"
      },
      "year_of_birth": 2006,
      "month_of_birth": 3,
      "day_of_birth": 19,
      "birth_datetime": "2006-03-19T00:00:00Z",
      "gender_source_value": "M",
      "race_source_value": "white",
      "ethnicity_source_value": "nonhispanic",
      "ethnicity_source_concept_id": 0
    },
    {
      "person_id": 226994,
      "gender_concept": {
        "concept_id": 8507,
        "concept_name": "MALE"
      },
      "race_concept": {
        "concept_id": 8527,
        "concept_name": "White"
      },
      "year_of_birth": 2001,
      "month_of_birth": 5,
      "day_of_birth": 30,
      "birth_datetime": "2001-05-30T00:00:00Z",
      "gender_source_value": "M",
      "race_source_value": "white",
      "ethnicity_source_value": "nonhispanic",
      "ethnicity_source_concept_id": 0
    }
  ]
}

```
### visit_occurrence
### condition_occurrence
### drug_exposure
### death




# Troubleshooting

## 이미 존재하는 db schema를 django models 로 인식

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

- person.gender_concept, person.gender_source_value 이유?
