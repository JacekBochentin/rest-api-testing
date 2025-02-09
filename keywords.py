import requests

class RESTAPIKeywords:
    def __init__(self):
        self.base_url = "http://localhost:3000"
        self.headers = {"Authorization": "Bearer 12345"}

    def _make_request(self, method, endpoint, **kwargs):
        """Make an HTTP request and return the response."""
        url = f"{self.base_url}{endpoint}"
        response = requests.request(method, url, headers=self.headers, **kwargs)
        return response

    def _assert_status_code(self, response, expected_code):
        """Check if the response status code matches the expected code."""
        assert response.status_code == expected_code, \
            f"Expected status {expected_code}, but got {response.status_code}"

    def _assert_response_contains(self, response, key, expected_value=None):
        """Check if the response contains the specified key and value."""
        json_data = response.json()
        assert key in json_data, f"Response does not contain key: {key}"
        if expected_value is not None:
            assert json_data[key] == expected_value, \
                f"Expected {expected_value} for key {key}, but got {json_data[key]}"

    def get_users(self):
        """Get all active users and check if the status is 200."""
        response = self._make_request("GET", "/users")
        self._assert_status_code(response, 200)
        return response.json()

    def get_user_by_id(self, user_id, expected_name=None):
        """Get user by ID and check if the status is 200."""
        response = self._make_request("GET", f"/users/{user_id}")
        self._assert_status_code(response, 200)
        if expected_name:
            self._assert_response_contains(response, "name", expected_name)
        return response.json()

    def create_user(self, name, age, city):
        """Create a new user and check if the status is 201."""
        data = {"name": name, "age": age, "city": city}
        response = self._make_request("POST", "/users", json=data)
        self._assert_status_code(response, 201)
        self._assert_response_contains(response, "name", name)
        return response.json()

    def update_user(self, user_id, **kwargs):
        """Update user by ID and check if the status is 200."""
        response = self._make_request("PUT", f"/users/{user_id}", json=kwargs)
        self._assert_status_code(response, 200)
        return response.json()

    def patch_user(self, user_id, **kwargs):
        """Partially update user by ID and check if the status is 200."""
        response = self._make_request("PATCH", f"/users/{user_id}", json=kwargs)
        self._assert_status_code(response, 200)
        return response.json()

    def soft_delete_user(self, user_id):
        """Soft delete user by ID and check if the status is 204."""
        response = self._make_request("DELETE", f"/users/{user_id}")
        self._assert_status_code(response, 204)

    def get_all_users_including_deleted(self):
        """Get all users, including deleted ones, and check if the status is 200."""
        response = self._make_request("GET", "/users/all")
        self._assert_status_code(response, 200)
        return response.json()

    def reset_rest_api(self):
        """Reset the REST API state and check if the status is 200."""
        response = self._make_request("POST", "/reset")
        self._assert_status_code(response, 200)