# 개발환경

```
$ uname -a
Linux hm-xpse15 5.3.0-19-generic #20-Ubuntu SMP Fri Oct 18 09:04:39 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux

$ python -V
Python 3.8.10

```
편집기: Emacs

# 설정

## DB 접속

아래 값을 shell의 환경변수에 등록합니다.

```
export DB_NAME="synthe~"
export DB_USER="walke~"
export DB_PW="******"
export DB_HOST="localhost"
```

# 실행
## 패키지 설치

파이썬 가상 환경 준비후 설치합니다.

```
$ pip install -r requirements.txt
```

```
$ python manage.py runserver
```

# 접근 가능 endpoints

## 구현된 endpoints

- http://localhost:8000/stat/patient/
- http://localhost:8000/stat/visit/
- http://localhost:8000/concept/\?search\=gender
- http://localhost:8000/person/\?search\=hispanic
- http://localhost:8000/visitoccurrence/\?search\=encounter
- http://localhost:8000/conditionoccurrence/\?search\=bronch
- http://localhost:8000/drugexposure/
- http://localhost:8000/death/\?search\=match

## swagger
- http://localhost:8000/schema/


# 확인

## exam_1

*환자와 방문 테이블들의 간단한 통계를 제공하는 API를 구현합니다.*

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

*각 테이블에 사용된 concept_id들의 정보를 얻을 수 있는 API를 만듭니다.*

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

*각 테이블의 row를 조회하는 API를 구현합니다.*

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
```
$ curl http://localhost:8000/visitoccurrence/\?search\=encounter | jq .

{
  "count": 41810,
  "next": "http://localhost:8000/visitoccurrence/?limit=5&offset=5&search=encounter",
  "previous": null,
  "results": [
    {
      "visit_occurrence_id": 2482686,
      "visit_concept": {
        "concept_id": 9201,
        "concept_name": "Inpatient Visit"
      },
      "visit_type_concept": {
        "concept_id": 44818517,
        "concept_name": "Visit derived from encounter on claim"
      },
      "visit_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "discharge_to_concept": null,
      "visit_start_date": "2020-03-10",
      "visit_start_datetime": "2020-03-10T15:53:50Z",
      "visit_end_date": "2020-03-18",
      "visit_end_datetime": "2020-03-18T20:40:50Z",
      "provider_id": null,
      "care_site_id": null,
      "visit_source_value": "b9438697-173d-4256-96c2-fcbb0f9cdf87",
      "admitted_from_concept_id": 0,
      "admitted_from_source_value": null,
      "discharge_to_source_value": "0",
      "person": 2293584,
      "preceding_visit_occurrence": 87633782
    },
    {
      "visit_occurrence_id": 3533806,
      "visit_concept": {
        "concept_id": 9201,
        "concept_name": "Inpatient Visit"
      },
      "visit_type_concept": {
        "concept_id": 44818517,
        "concept_name": "Visit derived from encounter on claim"
      },
      "visit_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "discharge_to_concept": null,
      "visit_start_date": "2018-10-05",
      "visit_start_datetime": "2018-10-05T09:45:37Z",
      "visit_end_date": "2018-10-06",
      "visit_end_datetime": "2018-10-06T10:45:37Z",
      "provider_id": null,
      "care_site_id": null,
      "visit_source_value": "8529614a-c0af-44c4-966e-240142628f67",
      "admitted_from_concept_id": 0,
      "admitted_from_source_value": null,
      "discharge_to_source_value": "0",
      "person": 2460892,
      "preceding_visit_occurrence": 323658
    },
    {
      "visit_occurrence_id": 2657368,
      "visit_concept": {
        "concept_id": 9201,
        "concept_name": "Inpatient Visit"
      },
      "visit_type_concept": {
        "concept_id": 44818517,
        "concept_name": "Visit derived from encounter on claim"
      },
      "visit_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "discharge_to_concept": null,
      "visit_start_date": "2017-04-02",
      "visit_start_datetime": "2017-04-02T10:42:34Z",
      "visit_end_date": "2017-04-03",
      "visit_end_datetime": "2017-04-03T11:22:34Z",
      "provider_id": null,
      "care_site_id": null,
      "visit_source_value": "f2bae24d-68ad-4029-a402-eaadf5e7e463",
      "admitted_from_concept_id": 0,
      "admitted_from_source_value": null,
      "discharge_to_source_value": "0",
      "person": 2348101,
      "preceding_visit_occurrence": 78269051
    },
    {
      "visit_occurrence_id": 211175,
      "visit_concept": {
        "concept_id": 9201,
        "concept_name": "Inpatient Visit"
      },
      "visit_type_concept": {
        "concept_id": 44818517,
        "concept_name": "Visit derived from encounter on claim"
      },
      "visit_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "discharge_to_concept": null,
      "visit_start_date": "2017-09-06",
      "visit_start_datetime": "2017-09-06T09:45:08Z",
      "visit_end_date": "2017-10-04",
      "visit_end_datetime": "2017-10-04T13:06:08Z",
      "provider_id": null,
      "care_site_id": null,
      "visit_source_value": "4f6b0f2b-6d69-4e50-b902-4a8e2d244e9b",
      "admitted_from_concept_id": 0,
      "admitted_from_source_value": null,
      "discharge_to_source_value": "0",
      "person": 886110,
      "preceding_visit_occurrence": 2411579
    },
    {
      "visit_occurrence_id": 81431,
      "visit_concept": {
        "concept_id": 9201,
        "concept_name": "Inpatient Visit"
      },
      "visit_type_concept": {
        "concept_id": 44818517,
        "concept_name": "Visit derived from encounter on claim"
      },
      "visit_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "discharge_to_concept": null,
      "visit_start_date": "2018-01-11",
      "visit_start_datetime": "2018-01-11T20:54:59Z",
      "visit_end_date": "2018-01-12",
      "visit_end_datetime": "2018-01-12T20:54:59Z",
      "provider_id": null,
      "care_site_id": null,
      "visit_source_value": "8d6c5544-36b3-48c7-a02d-1ad81e769959",
      "admitted_from_concept_id": 0,
      "admitted_from_source_value": null,
      "discharge_to_source_value": "0",
      "person": 1769327,
      "preceding_visit_occurrence": 10917709
    }
  ]
}

```

### condition_occurrence

```
$ curl http://localhost:8000/conditionoccurrence/\?search\=bronch | jq .

{
  "count": 506,
  "next": "http://localhost:8000/conditionoccurrence/?limit=5&offset=5&search=bronch",
  "previous": null,
  "results": [
    {
      "condition_occurrence_id": 1466186,
      "condition_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_type_concept": {
        "concept_id": 32020,
        "concept_name": "EHR encounter diagnosis"
      },
      "condition_source_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_start_date": "2012-10-23",
      "condition_start_datetime": "2012-10-23T00:00:00Z",
      "condition_end_date": "2012-10-30",
      "condition_end_datetime": "2012-10-30T00:00:00Z",
      "stop_reason": null,
      "provider_id": null,
      "visit_detail_id": 0,
      "condition_source_value": "10509002",
      "condition_status_source_value": null,
      "person": 116496,
      "condition_status_concept": 0,
      "visit_occurrence": 36112948
    },
    {
      "condition_occurrence_id": 11162525,
      "condition_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_type_concept": {
        "concept_id": 32020,
        "concept_name": "EHR encounter diagnosis"
      },
      "condition_source_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_start_date": "2018-11-07",
      "condition_start_datetime": "2018-11-07T00:00:00Z",
      "condition_end_date": "2018-11-14",
      "condition_end_datetime": "2018-11-14T00:00:00Z",
      "stop_reason": null,
      "provider_id": null,
      "visit_detail_id": 0,
      "condition_source_value": "10509002",
      "condition_status_source_value": null,
      "person": 886110,
      "condition_status_concept": 0,
      "visit_occurrence": 31254220
    },
    {
      "condition_occurrence_id": 5011695,
      "condition_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_type_concept": {
        "concept_id": 32020,
        "concept_name": "EHR encounter diagnosis"
      },
      "condition_source_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_start_date": "2014-09-25",
      "condition_start_datetime": "2014-09-25T00:00:00Z",
      "condition_end_date": "2014-10-09",
      "condition_end_datetime": "2014-10-09T00:00:00Z",
      "stop_reason": null,
      "provider_id": null,
      "visit_detail_id": 0,
      "condition_source_value": "10509002",
      "condition_status_source_value": null,
      "person": 397813,
      "condition_status_concept": 0,
      "visit_occurrence": 31070540
    },
    {
      "condition_occurrence_id": 20891721,
      "condition_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_type_concept": {
        "concept_id": 32020,
        "concept_name": "EHR encounter diagnosis"
      },
      "condition_source_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_start_date": "2017-12-16",
      "condition_start_datetime": "2017-12-16T00:00:00Z",
      "condition_end_date": "2017-12-23",
      "condition_end_datetime": "2017-12-23T00:00:00Z",
      "stop_reason": null,
      "provider_id": null,
      "visit_detail_id": 0,
      "condition_source_value": "10509002",
      "condition_status_source_value": null,
      "person": 1658282,
      "condition_status_concept": 0,
      "visit_occurrence": 89464894
    },
    {
      "condition_occurrence_id": 4863236,
      "condition_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_type_concept": {
        "concept_id": 32020,
        "concept_name": "EHR encounter diagnosis"
      },
      "condition_source_concept": {
        "concept_id": 260139,
        "concept_name": "Acute bronchitis"
      },
      "condition_start_date": "2019-03-22",
      "condition_start_datetime": "2019-03-22T00:00:00Z",
      "condition_end_date": "2019-04-05",
      "condition_end_datetime": "2019-04-05T00:00:00Z",
      "stop_reason": null,
      "provider_id": null,
      "visit_detail_id": 0,
      "condition_source_value": "10509002",
      "condition_status_source_value": null,
      "person": 386051,
      "condition_status_concept": 0,
      "visit_occurrence": 123947029
    }
  ]
}
```

### drug_exposure
```
$ curl http://localhost:8000/drugexposure/ | jq .
{
  "count": 46579,
  "next": "http://localhost:8000/drugexposure/?limit=5&offset=5",
  "previous": null,
  "results": [
    {
      "drug_exposure_id": 40900862,
      "drug_concept": {
        "concept_id": 19073183,
        "concept_name": "amoxicillin 250 MG Oral Capsule"
      },
      "drug_type_concept": {
        "concept_id": 38000177,
        "concept_name": "Prescription written"
      },
      "route_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "drug_source_concept": {
        "concept_id": 19073183,
        "concept_name": "amoxicillin 250 MG Oral Capsule"
      },
      "drug_exposure_start_date": "2017-05-04",
      "drug_exposure_start_datetime": "2017-05-04T01:41:54Z",
      "drug_exposure_end_date": "2017-05-18",
      "drug_exposure_end_datetime": "2017-05-18T01:41:54Z",
      "verbatim_end_date": "2017-05-18",
      "stop_reason": null,
      "refills": 0,
      "quantity": "0.0000000000",
      "days_supply": 14,
      "sig": null,
      "lot_number": "0",
      "provider_id": 0,
      "visit_detail_id": 0,
      "drug_source_value": "308182",
      "route_source_value": null,
      "dose_unit_source_value": null,
      "person": 26922,
      "visit_occurrence": 99499216
    },
    {
      "drug_exposure_id": 40757313,
      "drug_concept": {
        "concept_id": 40231925,
        "concept_name": "acetaminophen 325 MG / oxycodone hydrochloride 5 MG Oral Tablet"
      },
      "drug_type_concept": {
        "concept_id": 38000177,
        "concept_name": "Prescription written"
      },
      "route_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "drug_source_concept": {
        "concept_id": 40231925,
        "concept_name": "acetaminophen 325 MG / oxycodone hydrochloride 5 MG Oral Tablet"
      },
      "drug_exposure_start_date": "2016-07-24",
      "drug_exposure_start_datetime": "2016-07-24T13:28:53Z",
      "drug_exposure_end_date": "2016-09-23",
      "drug_exposure_end_datetime": "2016-09-23T13:28:53Z",
      "verbatim_end_date": "2016-09-23",
      "stop_reason": null,
      "refills": 0,
      "quantity": "0.0000000000",
      "days_supply": 61,
      "sig": null,
      "lot_number": "0",
      "provider_id": 0,
      "visit_detail_id": 0,
      "drug_source_value": "1049221",
      "route_source_value": null,
      "dose_unit_source_value": null,
      "person": 2955,
      "visit_occurrence": 9251642
    },
    {
      "drug_exposure_id": 52808614,
      "drug_concept": {
        "concept_id": 40229134,
        "concept_name": "acetaminophen 21.7 MG/ML / dextromethorphan hydrobromide 1 MG/ML / doxylamine succinate 0.417 MG/ML Oral Solution"
      },
      "drug_type_concept": {
        "concept_id": 38000177,
        "concept_name": "Prescription written"
      },
      "route_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "drug_source_concept": {
        "concept_id": 40229134,
        "concept_name": "acetaminophen 21.7 MG/ML / dextromethorphan hydrobromide 1 MG/ML / doxylamine succinate 0.417 MG/ML Oral Solution"
      },
      "drug_exposure_start_date": "2015-04-02",
      "drug_exposure_start_datetime": "2015-04-02T13:28:53Z",
      "drug_exposure_end_date": "2015-04-16",
      "drug_exposure_end_datetime": "2015-04-16T13:28:53Z",
      "verbatim_end_date": "2015-04-16",
      "stop_reason": null,
      "refills": 0,
      "quantity": "0.0000000000",
      "days_supply": 14,
      "sig": null,
      "lot_number": "0",
      "provider_id": 0,
      "visit_detail_id": 0,
      "drug_source_value": "1043400",
      "route_source_value": null,
      "dose_unit_source_value": null,
      "person": 2955,
      "visit_occurrence": 57618650
    },
    {
      "drug_exposure_id": 52808615,
      "drug_concept": {
        "concept_id": 1115171,
        "concept_name": "naproxen sodium 220 MG Oral Tablet"
      },
      "drug_type_concept": {
        "concept_id": 38000177,
        "concept_name": "Prescription written"
      },
      "route_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "drug_source_concept": {
        "concept_id": 1115171,
        "concept_name": "naproxen sodium 220 MG Oral Tablet"
      },
      "drug_exposure_start_date": "2016-07-24",
      "drug_exposure_start_datetime": "2016-07-24T13:28:53Z",
      "drug_exposure_end_date": "2016-08-23",
      "drug_exposure_end_datetime": "2016-08-23T13:28:53Z",
      "verbatim_end_date": "2016-08-23",
      "stop_reason": null,
      "refills": 0,
      "quantity": "0.0000000000",
      "days_supply": 30,
      "sig": null,
      "lot_number": "0",
      "provider_id": 0,
      "visit_detail_id": 0,
      "drug_source_value": "849574",
      "route_source_value": null,
      "dose_unit_source_value": null,
      "person": 2955,
      "visit_occurrence": 9251642
    },
    {
      "drug_exposure_id": 111107864,
      "drug_concept": {
        "concept_id": 40213154,
        "concept_name": "Influenza, seasonal, injectable, preservative free"
      },
      "drug_type_concept": {
        "concept_id": 581452,
        "concept_name": "Dispensed in Outpatient office"
      },
      "route_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "drug_source_concept": {
        "concept_id": 40213154,
        "concept_name": "Influenza, seasonal, injectable, preservative free"
      },
      "drug_exposure_start_date": "2011-04-04",
      "drug_exposure_start_datetime": "2011-04-04T13:28:53Z",
      "drug_exposure_end_date": "2011-04-04",
      "drug_exposure_end_datetime": "2011-04-04T13:28:53Z",
      "verbatim_end_date": "2011-04-04",
      "stop_reason": null,
      "refills": 0,
      "quantity": "0.0000000000",
      "days_supply": 0,
      "sig": null,
      "lot_number": "0",
      "provider_id": 0,
      "visit_detail_id": 0,
      "drug_source_value": "140",
      "route_source_value": null,
      "dose_unit_source_value": null,
      "person": 2955,
      "visit_occurrence": 57618654
    }
  ]
}


```

### death
```
$ curl http://localhost:8000/death/\?search\=match | jq .

{
  "count": 152,
  "next": "http://localhost:8000/death/?limit=5&offset=5&search=match",
  "previous": null,
  "results": [
    {
      "person": 1691806,
      "cause_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "cause_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "death_date": "2015-06-02",
      "death_datetime": null,
      "death_type_concept_id": 32815,
      "cause_source_value": 233604007
    },
    {
      "person": 99181,
      "cause_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "cause_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "death_date": "2018-11-04",
      "death_datetime": null,
      "death_type_concept_id": 32815,
      "cause_source_value": 87433001
    },
    {
      "person": 2738610,
      "cause_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "cause_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "death_date": "1998-03-28",
      "death_datetime": null,
      "death_type_concept_id": 32815,
      "cause_source_value": 262574004
    },
    {
      "person": 31196,
      "cause_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "cause_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "death_date": "2020-03-16",
      "death_datetime": null,
      "death_type_concept_id": 32815,
      "cause_source_value": 840539006
    },
    {
      "person": 994339,
      "cause_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "cause_source_concept": {
        "concept_id": 0,
        "concept_name": "No matching concept"
      },
      "death_date": "2006-03-08",
      "death_datetime": null,
      "death_type_concept_id": 32815,
      "cause_source_value": 22298006
    }
  ]
}


```




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

# 마무리

- 같은 목적을 가진 서로 다른 두개의 컬럼이 존재합니다. 특별한 이유가 있을까요?

예) person.gender_concept, person.gender_source_value 이유?

- 제안: 응답 속도를 개선
  - 방문시 연령대(10세 단위)별 방문 수
  
  방문 시점의 나이를 계산하기 위해서, 환자의 생년(person.birth_datetime)과 방문일시(VisitOccurrence.visit_start_datetime)를 계산해야 했습니다. 연령대별 방문 수를 자주 계산해야 한다면 미리 계산된 값을 저장하는 것도 응답속도를 개선하기 위한 방법이 될 것 같습니다.
  - 통계 대상이 되는 데이터 양이 크다면, 그리고 통계값이 어느정도 실시간성이 아니라면, 주기적으로 background(celery) 서버가 해당 계산을 하고, api 요청시 계산된 값을 반환하는 접근도 고민해 보면 좋겠습니다.
- 
