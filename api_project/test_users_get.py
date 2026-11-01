import pytest
from jsonschema import validate
from schemas.user_schemas import USERS_LIST_SCHEMA, USER_SCHEMA

def test_get_users_list(api_client, base_url):
    response = api_client.get(
        f"{base_url}/users"
    )

    user_schema = USERS_LIST_SCHEMA

    assert response.status_code == 200

    body = response.json()
    user = body["data"]
    validate(instance = body, schema = user_schema)
    assert len(user) > 0

def assert_user_fields(users):
    assert "id" in users
    assert users["id"] == 3

def test_get_users_from_id(api_client, base_url):
    response = api_client.get(
        f"{base_url}/users/3"
    )

    assert response.status_code == 200

    user_schema = USER_SCHEMA
    body = response.json()
    #user = body["data"]
    validate(instance = body["data"], schema = user_schema)
    assert_user_fields(body["data"])

@pytest.mark.parametrize("user_id", [1, 2, 4])
def test_get_users_with_parametrize(user_id, api_client, base_url):
    response = api_client.get(
        f"{base_url}/users/{user_id}"
    )

    assert response.status_code == 200
    body = response.json()
    user = body["data"]
    assert user_id == user["id"]



