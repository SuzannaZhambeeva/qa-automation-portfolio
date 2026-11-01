import requests

def test_create_user(api_client, base_url):
    response = api_client.post(
        f"{base_url}/users",
        json = {"name": "Anna", "job": "tester"}
    )

    assert response.status_code == 201

    body = response.json()
    assert body["name"] == "Anna"
    assert body["job"] == "tester"
    assert body["id"] is not None
    assert body["id"] != "" 

def test_check_put_user(api_client, base_url):
    response = api_client.put(
        f"{base_url}/users/2",
        json = {"name": "Anna", "job": "senior tester"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["name"] == "Anna"
    assert body["job"] == "senior tester"
    assert "updatedAt" in body

def test_check_patch_user(api_client, base_url):
    response = api_client.patch(
        f"{base_url}/users/2",
        json = {"job": "lead tester"}
    )

    assert response.status_code == 200

    body = response.json()
    assert body["job"] == "lead tester"

def test_delete_user(api_client, base_url):
    response = api_client.delete(
        f"{base_url}/users/2",
    )

    assert response.status_code == 204
    assert response.text == ""