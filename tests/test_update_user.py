import requests
from jsonschema.validators import validate
from conftest import load_json_schema


def test_successful_update_user_():
    response = requests.patch(
        'https://reqres.in/api/users/2',
        {"name": "Elena",
         "job": "QA Automation Engineer"}
    )

    assert response.status_code == 200
    assert response.json()['name'] == "Elena"
    assert response.json()['job'] == "QA Automation Engineer"


def test_update_user_schema_response_format():
    schema = load_json_schema('patch_update_user_schema_response.json')

    response = requests.patch(
        'https://reqres.in/api/users/2',
        {"name": "Elena",
         "job": "QA Automation Engineer"})

    validate(instance=response.json(),
             schema=schema)
