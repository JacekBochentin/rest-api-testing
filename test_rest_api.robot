*** Settings ***
Library    keywords.RESTAPIKeywords
Suite Setup       Reset REST API
Suite Teardown    Reset REST API

*** Test Cases ***
Get All Users
    Get Users

Get User By ID
    Get User By Id    1    expected_name=Jan Kowalski

Create New User
    Create User    name=Marek Nowak    age=40    city=Poznań

Update User
    Update User    1    name=Jan Nowak    age=31    city=Warszawa

Patch User
    Patch User    2    age=26

Soft Delete User
    Soft Delete User    1
    ${users} =    Get All Users
    Should Not Contain    ${users}    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": false}

Get All Users Including Deleted
    Soft Delete User    1
    ${users} =    Get All Users Including Deleted
    Should Contain    ${users}    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": true}