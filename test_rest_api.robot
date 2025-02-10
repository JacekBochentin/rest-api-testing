*** Settings ***
Library    keywords.py    WITH NAME    API    # Użyj WITH NAME, aby nadać alias
# Suite Setup       API.Reset Rest Api
# Suite Teardown    API.Reset Rest Api
Test Setup        API.Reset Rest Api
Test Teardown     API.Reset Rest Api

*** Test Cases ***
Get All Users
    API.Get Users

Get User By ID
    API.Get User By Id    1    expected_name=Jan Kowalski

Create New User
    API.Create User    name=Marek Nowak    age=40    city=Poznań

Update User
    API.Update User    1    name=Jan Nowak    age=31    city=Warszawa

Patch User
    API.Patch User    2    age=26

Soft Delete User
    API.Soft Delete User    1
    ${users} =    API.Get Users
    Should Not Contain    ${users}    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": false}

Get All Users Including Deleted
    API.Soft Delete User    1
    ${users} =    API.Get All Users Including Deleted
    ${expected_user} =    Evaluate    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": True}
    Should Contain    ${users}    ${expected_user}