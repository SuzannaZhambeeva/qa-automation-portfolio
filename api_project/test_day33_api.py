import os
import pytest
import requests


API_KEY = os.environ.get("REQRES_API_KEY")

HEADERS = {"x-api-key": API_KEY}

@pytest.mark.parametrize("id", [1, 2, 3])
def test_get_user_with_param(api_client, base_url, id):
    response = api_client.get(
        f"{base_url}/users/{id}",
    )

    assert response.status_code == 200

    body = response.json()
    assert body["data"]["id"] == id

def test_user_create(base_url):
    response = requests.post(
        f"{base_url}/users",
         headers=HEADERS,
         json = {
             "name": "Playwright",
             "job": "tester"
         }
    )

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == "Playwright"