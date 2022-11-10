import requests
import random

# User operations Tests
# TC001: Creating a user with all field included
def test_ProperUser(initVariables):
    userid = initVariables["userid"]
    firstName = initVariables["firstName"]
    lastName = initVariables   ["lastName"]
    baseURL = initVariables["baseURL"]
    user = {"id":userid, "username": firstName.lower()+lastName.lower(), "firstName": firstName, "lastName": lastName, "email": firstName.lower()+lastName.lower()+"@yopmail.com", "password":"password", "phone":random.randint(1000000000, 9999999999), "userStatus": 0}
    response = requests.post(baseURL+"user", json=user)
    assert response.status_code == 200 and len(response.json()["message"])>0

# TC002: Creating a user with a random field missing
def test_OneMissingField(initVariables):
    userid = initVariables["userid"]
    firstName = initVariables["firstName"]
    lastName = initVariables   ["lastName"]
    baseURL = initVariables["baseURL"]
    user = {"id":userid, "username": firstName.lower()+lastName.lower(), "firstName": firstName, "lastName": lastName, "email": firstName.lower()+lastName.lower()+"@yopmail.com", "password":"password", "phone":random.randint(1000000000, 9999999999), "userStatus": 0}
    num = random.randint(0,7)
    user.pop(list(user.keys())[num], None)
    response = requests.post(baseURL+"user", json=user)
    assert response.status_code == 400 and len(response.json()["message"])>0

# TC003: Creating a user with an extra field included
def test_ExtraField(initVariables):
    userid = initVariables["userid"]
    firstName = initVariables["firstName"]
    lastName = initVariables   ["lastName"]
    baseURL = initVariables["baseURL"]
    user = {"id":userid, "username": firstName.lower()+lastName.lower(), "firstName": firstName, "lastName": lastName, "email": firstName.lower()+lastName.lower()+"@yopmail.com", "password":"password", "phone":random.randint(1000000000, 9999999999), "userStatus": 0, "randomField":int(random.random()*10)}
    response = requests.post(baseURL+"user", json=user)
    assert response.status_code == 400 and len(response.json()["message"])>0

# TC004: Improperly formed ID i.e. returns a string for some reason
def test_ExtraField(initVariables):
    firstName = initVariables["firstName"]
    lastName = initVariables   ["lastName"]
    baseURL = initVariables["baseURL"]
    user = {"id":"userid", "username": firstName.lower()+lastName.lower(), "firstName": firstName, "lastName": lastName, "email": firstName.lower()+lastName.lower()+"@yopmail.com", "password":"password", "phone":random.randint(1000000000, 9999999999), "userStatus": 0}
    response = requests.post(baseURL+"user", json=user)
    assert response.status_code == 400 and len(response.json()["message"])>0
