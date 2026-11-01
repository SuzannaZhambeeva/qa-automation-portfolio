import pytest
import requests
import os

API_KEY = os.environ.get("REQRES_API_KEY")

@pytest.fixture
def product():
    return {
        "name": "Laptop",
        "price": 1000,
        "in_stock": True
        }

@pytest.fixture
def users():
    return{
        "username": "test_user", 
        "email": "test@mail.com", 
        "is_active": True, 
        "score": 42
    }

@pytest.fixture
def numbers():
    return [1, 2, 3, 4, 5]

@pytest.fixture
def cart():
    return{
        "items":["apple", "bread", "milk"], 
        "total": 350, 
        "is_paid": False
    }

@pytest.fixture
def headers():
    return {"x-api-key": API_KEY}

@pytest.fixture
def base_url():
    return "https://reqres.in/api"

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update({"x-api-key": API_KEY})
    return session

@pytest.fixture
def auth_session():
    session = requests.Session()
    session.headers.update({"x-api-key": API_KEY})
    
    # логинимся один раз
    response = session.post(
        "https://reqres.in/api/login",
        json={"email": "eve.holt@reqres.in", "password": "cityslicka"}
    )
    token = response.json()["token"]
    
    # добавляем токен в сессию
    session.headers.update({"Authorization": f"Bearer {token}"})
    
    return session

@pytest.fixture
def new_user():
    response = requests.post(
        "https://reqres.in/api/users",
        headers={"x-api-key": API_KEY},
        json={"name": "Anna", "job": "tester"}
    )

    body = response.json()
    user_id = body["id"]

    return user_id

@pytest.fixture
def new_user_full():
    response = requests.post(
        "https://reqres.in/api/users",
        headers={"x-api-key": API_KEY},
        json={"name": "Anna", "job": "tester"}
    )
    
    body = response.json()
    return body
