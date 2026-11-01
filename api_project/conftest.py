import os
import pytest
import requests

API_KEY = os.environ.get("REQRES_API_KEY")
HEADERS = {"x-api-key": API_KEY}

@pytest.fixture
def api_client():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session

@pytest.fixture
def base_url():
    return "https://reqres.in/api"