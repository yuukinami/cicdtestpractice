
import random
import pytest

@pytest.fixture
def initVariables():
    baseURL = "https://petstore.swagger.io/v2/"
    firstNames = ["Morgan", "Yuki", "Yeamin", "Tully", "Nami", "Lola", "Mika"]
    lastNames = ["Hodges", "Khan", "Bunch"]
    firstName = firstNames[random.randint(0,len(firstNames)-1)]
    lastName = lastNames[random.randint(0,len(lastNames)-1)]
    userid = random.randint(100000, 999999)

    return {"baseURL":baseURL, "firstName":firstName, "lastName":lastName, "userid":userid}