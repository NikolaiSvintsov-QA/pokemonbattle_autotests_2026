import pytest
import requests
from config.settings import BASE_URL, TOKEN
from pprint import pprint



def test_get_me_smoke():
    headers = {
        "trainer_token": TOKEN
    }

    response = requests.get(f"{BASE_URL}/me", headers=headers)

    data = response.json()
    trainer = data["data"][0]
    
    pprint(data)
    
    # print("Data:", data)
    # print(type(response))
    # print(type(response.json()))


    assert response.status_code == 200, "Status code is not 200"
    assert "status" in data, "Response does not contain 'status' key"
    assert "data" in data, "Response does not contain 'data' key"


    assert "id" in trainer, "Trainer does not contain 'id' key"
    assert "trainer_name" in trainer, "Trainer does not contain 'trainer_name' key"
    assert "level" in trainer, "Trainer does not contain 'level' key"
   
    assert isinstance(trainer["id"], str)
    assert isinstance(trainer["trainer_name"], str)
    assert isinstance(trainer["level"], str)


def test_get_me_without_token():
    response = requests.get(f"{BASE_URL}/me")

    # pprint(response.status_code) 

    assert response.status_code in (401,422), "Status code is not 401 or 422"

def test_get_me_without_invalid_token():
    headers = {
        "trainer_token": "invalid_token"
    }

    response = requests.get(f"{BASE_URL}/me", headers=headers)
    # pprint(response.status_code)

    assert response.status_code in (401,422), "Status code is not 401 or 422"

def test_get_me_wrong_method():
    headers = {
        "trainer_token": TOKEN
    }

    response = requests.post(f"{BASE_URL}/me", headers=headers)
    # pprint(response.status_code)

    assert response.status_code == 405, "Status code is not 405"


