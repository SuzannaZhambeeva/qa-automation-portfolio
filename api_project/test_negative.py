import requests
import pytest

def test_negative_users(api_client, base_url):
    response = api_client.get(
        f"{base_url}/users/999"
    )

    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [998, 999, 1000])
def test_negative_user_with_parametrize(user_id, api_client, base_url):
    response = api_client.get(
        f"{base_url}/users/{user_id}"
    )

    assert response.status_code == 404

def test_delete_user_negative(api_client, base_url):
    response = api_client.delete(
        f"{base_url}/user/9981"
    )

    assert response.status_code == 204