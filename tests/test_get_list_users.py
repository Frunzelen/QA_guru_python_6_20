import requests
from jsonschema.validators import validate

from conftest import load_json_schema


def test_successful_get_list_users_by_page():
    page = 3
    response = requests.get('https://reqres.in/api/users', params={'page': page})

    assert response.status_code == 200
    assert response.json()['page'] == page


def test_successful_get_list_users_data_by_per_page():
    per_page = 5

    response = requests.get('https://reqres.in/api/users',
                            params={'per_page': per_page})

    assert response.status_code == 200
    assert response.json()['per_page'] == per_page
    assert len(response.json()['data']) == per_page


def test_get_list_users_schema_response_format():
    schema = load_json_schema('get_list_users_schema_response.json')

    response = requests.get('https://reqres.in/api/users')

    validate(instance=response.json(),
             schema=schema)
