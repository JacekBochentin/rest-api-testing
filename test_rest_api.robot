*** Settings ***
Library    keywords.py    WITH NAME    API  # Import the custom Python file (keywords.py) and give it the alias 'API'
# Suite Setup       API.Reset Rest Api  # Optionally, reset the API state before any tests run (this is commented out)
# Suite Teardown    API.Reset Rest Api  # Optionally, reset the API state after all tests run (this is commented out)
Test Setup        API.Reset Rest Api  # Reset the API state before each test case runs
Test Teardown     API.Reset Rest Api  # Reset the API state after each test case runs

*** Test Cases ***
# Test Case 1: Get All Users
Get All Users
    API.Get Users  # Call the 'Get Users' keyword to retrieve all active users from the API

# Test Case 2: Get User By ID
Get User By ID
    API.Get User By Id    1    expected_name=Jan Kowalski  # Retrieve user with ID=1 and check that their name is "Jan Kowalski"

# Test Case 3: Create New User
Create New User
    API.Create User    name=Marek Nowak    age=40    city=Poznań  # Create a new user with the provided details (name, age, city)

# Test Case 4: Update User
Update User
    API.Update User    1    name=Jan Nowak    age=31    city=Warszawa  # Update user with ID=1 to change their name, age, and city

# Test Case 5: Patch User
Patch User
    API.Patch User    2    age=26  # Partially update user with ID=2, changing their age to 26

# Test Case 6: Soft Delete User
Soft Delete User
    API.Soft Delete User    1  # Soft delete user with ID=1
    ${users} =    API.Get Users  # Get the list of active users
    Should Not Contain    ${users}    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": false}  # Ensure that the deleted user is no longer in the active users list

# Test Case 7: Get All Users Including Deleted
Get All Users Including Deleted
    API.Soft Delete User    1  # Soft delete user with ID=1
    ${users} =    API.Get All Users Including Deleted  # Retrieve all users, including deleted ones
    ${expected_user} =    Evaluate    {"id": 1, "name": "Jan Kowalski", "age": 30, "city": "Warszawa", "deleted": True}  # Define the expected user data with "deleted" set to True
    Should Contain    ${users}    ${expected_user}  # Check if the deleted user is included in the list of all users
