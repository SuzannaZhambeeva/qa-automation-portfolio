import requests

def test_login_user(api_client, base_url):
    response = api_client.post(
        f"{base_url}/login",
        json = {"email": "eve.holt@reqres.in", 
                "password": "cityslicka"}
    )

    assert response.status_code == 200
    body = response.json()
    assert "token" in body
    assert body["token"] != ""

def test_login_user_without_password(api_client, base_url):
    response = api_client.post(
        f"{base_url}/login",
        json = {"email": "eve.holt@reqres.in"}
    )

    assert response.status_code == 400
    body = response.json()
    assert "error" in body

def test_login_user_with_auth_session(auth_session, base_url):
    response = auth_session.get(
        f"{base_url}/users",
    )

    assert response.status_code == 200

    body = response.json()
    assert isinstance(body["data"], list)