import requests
from jsonschema.validators import validate
from conftest import load_json_schema


def test_register_successful_user_():
    data = {"email": "eve.holt@reqres.in",
            "password": "pistol"}

    response = requests.post('https://reqres.in/api/register', data=data)

    assert response.status_code == 200


def test_register_unsuccessful_user_():
    data = {"email": "sydney@fife"}

    response = requests.post('https://reqres.in/api/register', data=data)

    assert response.json()['error'] == 'Missing password'


def test_register_successful_user_schema_response_format():
    schema = load_json_schema('post_register_user_schema_response.json')
    data = {"email": "eve.holt@reqres.in",
            "password": "pistol"}

    response = requests.post('https://reqres.in/api/register', data=data)

    validate(instance=response.json(),
             schema=schema)
