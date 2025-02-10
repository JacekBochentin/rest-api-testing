import requests  # Importing the requests library to make HTTP requests
from robot.api.deco import keyword, library  # Importing Robot Framework decorators

# Mark this class as a Robot Framework library, making it accessible in Robot test cases.
@library(scope='GLOBAL')  # This decorator indicates the library is global
class RESTAPIKeywords:
    
    # The __init__ method is called when an instance of the class is created.
    def __init__(self):
        self.base_url = "http://localhost:3000"  # This is the base URL of the REST API we will interact with.
        self.headers = {"Authorization": "Bearer 12345"}  # Authentication header for requests (dummy token).

    # This method sends an HTTP request based on the provided method (GET, POST, PUT, etc.)
    # and returns the response from the server.
    def make_request(self, method, endpoint, **kwargs):
        """Make an HTTP request and return the response."""
        url = f"{self.base_url}{endpoint}"  # Combine the base URL and the endpoint to form the full URL.
        response = requests.request(method, url, headers=self.headers, **kwargs)  # Make the request
        return response  # Return the response object

    # This method checks if the status code in the response matches the expected status code.
    def assert_status_code(self, response, expected_code):
        """Check if the response status code matches the expected code."""
        assert response.status_code == expected_code, \
            f"Expected status {expected_code}, but got {response.status_code}"  # Raise an error if codes don't match

    # This method checks if the response contains a specific key, and optionally checks its value.
    def assert_response_contains(self, response, key, expected_value=None):
        """Check if the response contains the specified key and value."""
        json_data = response.json()  # Parse the JSON data from the response
        assert key in json_data, f"Response does not contain key: {key}"  # Check if the key exists in the JSON data
        if expected_value is not None:
            # If expected_value is provided, check if the value for that key matches the expected value.
            assert json_data[key] == expected_value, \
                f"Expected {expected_value} for key {key}, but got {json_data[key]}"

    # This is a Robot Framework keyword that gets all active users and checks if the response status is 200.
    @keyword
    def get_users(self):
        """Get all active users and check if the status is 200."""
        response = self.make_request("GET", "/users")  # Send a GET request to the '/users' endpoint
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)
        return response.json()  # Return the list of users (as JSON)

    # This Robot Framework keyword gets a specific user by their ID and checks if the response status is 200.
    # If an expected name is provided, it checks if the name matches that.
    @keyword
    def get_user_by_id(self, user_id, expected_name=None):
        """Get user by ID and check if the status is 200."""
        response = self.make_request("GET", f"/users/{user_id}")  # Send a GET request with the user's ID
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)
        if expected_name:
            self.assert_response_contains(response, "name", expected_name)  # Check if the name matches the expected value
        return response.json()  # Return the user's data (as JSON)

    # This Robot Framework keyword creates a new user with the given data and checks if the status is 201.
    @keyword
    def create_user(self, name, age, city):
        """Create a new user and check if the status is 201."""
        data = {"name": name, "age": age, "city": city}  # Prepare the user data as a dictionary
        response = self.make_request("POST", "/users", json=data)  # Send a POST request to create the user
        self.assert_status_code(response, 201)  # Verify the status code is 201 (Created)
        self.assert_response_contains(response, "name", name)  # Verify the name of the created user
        return response.json()  # Return the created user's data (as JSON)

    # This Robot Framework keyword updates an existing user by their ID and checks if the status is 200.
    @keyword
    def update_user(self, user_id, **kwargs):
        """Update user by ID and check if the status is 200."""
        response = self.make_request("PUT", f"/users/{user_id}", json=kwargs)  # Send a PUT request to update the user
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)
        return response.json()  # Return the updated user's data (as JSON)

    # This Robot Framework keyword partially updates a user by their ID and checks if the status is 200.
    @keyword
    def patch_user(self, user_id, **kwargs):
        """Partially update user by ID and check if the status is 200."""
        response = self.make_request("PATCH", f"/users/{user_id}", json=kwargs)  # Send a PATCH request
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)
        return response.json()  # Return the partially updated user's data (as JSON)

    # This Robot Framework keyword deletes a user (soft delete) by their ID and checks if the status is 204.
    @keyword
    def soft_delete_user(self, user_id):
        """Soft delete user by ID and check if the status is 204."""
        response = self.make_request("DELETE", f"/users/{user_id}")  # Send a DELETE request to remove the user
        self.assert_status_code(response, 204)  # Verify the status code is 204 (No Content)

    # This Robot Framework keyword gets all users, including deleted ones, and checks if the status is 200.
    @keyword
    def get_all_users_including_deleted(self):
        """Get all users, including deleted ones, and check if the status is 200."""
        response = self.make_request("GET", "/users/all")  # Send a GET request to fetch all users, including deleted
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)
        return response.json()  # Return the list of users (as JSON)

    # This Robot Framework keyword resets the REST API to its initial state and checks if the status is 200.
    @keyword
    def reset_rest_api(self):
        """Reset the REST API state and check if the status is 200."""
        response = self.make_request("POST", "/reset")  # Send a POST request to reset the API
        self.assert_status_code(response, 200)  # Verify the status code is 200 (OK)

# Factory method to create an instance of the RESTAPIKeywords class.
def get_instance():
    return RESTAPIKeywords()  # Return an instance of the RESTAPIKeywords class
