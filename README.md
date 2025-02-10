# REST API Testing with Robot Framework

This project demonstrates how to test a simple REST API using Robot Framework. The REST API is built with Node.js and Express, and the tests are written in Robot Framework with custom Python keywords.

## What You'll Learn

### 1. **Building a REST API**
   - Learn how to create a REST API from scratch using **Node.js** and **Express**.
   - Understand the core concepts of REST, including:
     - HTTP methods (GET, POST, PUT, PATCH, DELETE).
     - Status codes (200, 201, 204, 404).
     - Request and response handling.
   - Implement features like:
     - CRUD operations (Create, Read, Update, Delete).
     - Soft delete functionality.
     - Filtering and sorting data.

### 2. **Automated Testing with Robot Framework**
   - Discover how to write **automated tests** for REST APIs using **Robot Framework**.
   - Learn how to create custom keywords in Python to simplify test cases.
   - Practice writing test scenarios for:
     - Validating API responses.
     - Testing edge cases (e.g., invalid inputs, missing data).
     - Verifying soft delete functionality.

### 3. **Best Practices in API Development and Testing**
   - Understand the importance of **clean code** and **modular design** in API development.
   - Learn how to use **setup and teardown** mechanisms to ensure consistent test environments.
   - Explore the concept of **soft delete** and why it's useful in real-world applications.

### 4. **End-to-End Workflow**
   - Follow a complete workflow from **API development** to **automated testing**.
   - Use the provided `setup.sh` (for Linux/macOS) or `setup.bat` (for Windows) script to automate the installation and execution of the project. 
   - Generate and analyze test reports to identify issues and improve code quality.

## Why This Project?

- **Practical Learning**: This project focuses on real-world scenarios, making it easier to apply what you learn to your own projects.
- **Step-by-Step Guidance**: The well-documented code and detailed SETUP section in this file make it easy to follow along, even if you're new to REST APIs or Robot Framework.
- **Open Source**: Feel free to fork, modify, and experiment with the code. Contributions are welcome!

## Who Is This For?

- **Beginners**: If you're new to REST APIs or automated testing, this project is a great starting point.
- **Experienced Developers**: If you're already familiar with REST APIs but want to learn Robot Framework, this project will help you get up to speed quickly.
- **Educators**: Use this project as a teaching resource in your coding bootcamps or workshops.

## Prerequisites

1. **Node.js**: Install from [https://nodejs.org](https://www.nodejs.org)
2. **Python**: Install from [https://www.python.org](https://www.python.org)

## Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/JacekBochentin/rest-api-testing.git
    cd rest-api-testing
    ```

2. Install dependencies for the REST API:

    ```bash
    npm install express
    ```

3. Install Python dependencies:

    ```bash
    pip install robotframework requests
    ```

4. Run the REST API:

    ```bash
    node rest_api.js
    ```

5. Run the tests:

    ```bash
    robot test_rest_api.robot
    ```

6. View the test report:

    Open the report.html

## Project Structure

- `rest_api.js`: The REST API code.
- `keywords.py`: Custom Python keywords for Robot Framework.
- `test_rest_api.robot`: Robot Framework test cases.
- `README.`]: This file.

## Endpoints

- **GET /users**: Get all active users.
- **GET /users/:id**: Get user by ID.
- **POST /users**: Create a new user.
- **PUT /users/:id**: Update user by ID.
- **PATCH /users/:id**: Partially update user by ID.
- **DELETE /users/:id**: Soft delete user by ID.
- **GET /users/all**: Get all users, including deleted ones.
- **POST /reset**: Reset the REST API state.

