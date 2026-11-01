import os
import pytest
import requests

API_KEY = os.environ.get("REQRES_API_KEY")

@pytest.mark.parametrize("id", [2, 4, 6])
def test_get_user(api_client, base_url, id):
    response = api_client.get(
        f"{base_url}/users/{id}",
    )

    assert response.status_code == 200

    body = response.json()
    assert body["data"]["id"] == id

def test_create_user(base_url):
    response = requests.post(
        f"{base_url}/users",
        headers={"x-api-key": API_KEY},
        json = {
            "name": "Playwright",
             "job": "tester"
        }
    )

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == "Playwright"