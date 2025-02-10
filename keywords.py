import requests
from robot.api.deco import keyword, library

@library(scope='GLOBAL')  # Dodaj ten dekorator
class RESTAPIKeywords:
    def __init__(self):
        self.base_url = "http://localhost:3000"
        self.headers = {"Authorization": "Bearer 12345"}

    def make_request(self, method, endpoint, **kwargs):
        """Make an HTTP request and return the response."""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        return response

    def assert_status_code(self, response, expected_code):
        """Check if the response status code matches the expected code."""
        assert response.status_code == expected_code, \
            f"Expected status {expected_code}, but got {response.status_code}"

    def assert_response_contains(self, response, key, expected_value=None):
        """Check if the response contains the specified key and value."""
        json_data = response.json()
        assert key in json_data, f"Response does not contain key: {key}"
        if expected_value is not None:
            assert json_data[key] == expected_value, \
                f"Expected {expected_value} for key {key}, but got {json_data[key]}"

    @keyword
    def get_users(self):
        """Get all active users and check if the status is 200."""
        response = self.make_request("GET", "/users")
        self.assert_status_code(response, 200)
        return response.json()

    @keyword
    def get_user_by_id(self, user_id, expected_name=None):
        """Get user by ID and check if the status is 200."""
        response = self.make_request("GET", f"/users/{user_id}")
        self.assert_status_code(response, 200)
        if expected_name:
            self.assert_response_contains(response, "name", expected_name)
        return response.json()

    @keyword
    def create_user(self, name, age, city):
        """Create a new user and check if the status is 201."""
        data = {"name": name, "age": age, "city": city}
        response = self.make_request("POST", "/users", json=data)
        self.assert_status_code(response, 201)
        self.assert_response_contains(response, "name", name)
        return response.json()

    @keyword
    def update_user(self, user_id, **kwargs):
        """Update user by ID and check if the status is 200."""
        response = self.make_request("PUT", f"/users/{user_id}", json=kwargs)
        self.assert_status_code(response, 200)
        return response.json()

    @keyword
    def patch_user(self, user_id, **kwargs):
        """Partially update user by ID and check if the status is 200."""
        response = self.make_request("PATCH", f"/users/{user_id}", json=kwargs)
        self.assert_status_code(response, 200)
        return response.json()

    @keyword
    def soft_delete_user(self, user_id):
        """Soft delete user by ID and check if the status is 204."""
        response = self.make_request("DELETE", f"/users/{user_id}")
        self.assert_status_code(response, 204)

    @keyword
    def get_all_users_including_deleted(self):
        """Get all users, including deleted ones, and check if the status is 200."""
        response = self.make_request("GET", "/users/all")
        self.assert_status_code(response, 200)
        return response.json()

    @keyword
    def reset_rest_api(self):
        """Reset the REST API state and check if the status is 200."""
        response = self.make_request("POST", "/reset")
        self.assert_status_code(response, 200)

# Factory method to return an instance of RESTAPIKeywords
def get_instance():
    return RESTAPIKeywords()