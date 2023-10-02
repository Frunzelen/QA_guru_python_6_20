import requests


def test_successful_test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/2')

    assert response.status_code == 204
