import requests
from jsonschema.validators import validate

from conftest import load_json_schema


def test_successful_create_user():
    data = {"name": "Elena",
         "job": "QA Automation Engineer"}
    response = requests.post('https://reqres.in/api/users', data=data)


    assert response.status_code == 201
    assert response.json()['name'] == 'Elena'
    assert response.json()['job'] == 'QA Automation Engineer'


def test_create_user_schema_response_format():
    schema = load_json_schema('post_create_user_schema_response_.json')

    data = {"name": "Elena",
            "job": "QA Automation Engineer"}
    response = requests.post('https://reqres.in/api/users', data=data)

    validate(response.json(), schema)
