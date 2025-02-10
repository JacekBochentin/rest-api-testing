// Import the express library to create an Express application
const express = require('express');
// Initialize an Express app
const app = express();

// Middleware to parse incoming JSON request bodies
app.use(express.json());

// Middleware for logging incoming requests and outgoing responses
app.use((req, res, next) => {
  console.log('--- Request ---');
  console.log(`Method: ${req.method}`);  // Log the HTTP method (e.g., GET, POST)
  console.log(`URL: ${req.originalUrl}`);  // Log the URL being requested
  console.log('Headers:', req.headers);  // Log the request headers
  console.log('Body:', req.body);  // Log the body of the request

  // Store the original `res.send` function to log the response before sending it
  const originalSend = res.send;
  res.send = function (body) {
    console.log('--- Response ---');
    console.log(`Status Code: ${res.statusCode}`);  // Log the status code of the response
    console.log('Body:', body);  // Log the response body
    originalSend.call(this, body);  // Send the response as usual
  };

  next();  // Pass control to the next middleware or route handler
});

// Initial list of users (this will act as a simple in-memory database)
let users = [
  { id: 1, name: "Jan Kowalski", age: 30, city: "Warszawa", deleted: false },
  { id: 2, name: "Anna Nowak", age: 25, city: "Kraków", deleted: false },
  { id: 3, name: "Piotr Wiśniewski", age: 35, city: "Warszawa", deleted: false },
  { id: 4, name: "Maria Kowalczyk", age: 28, city: "Gdańsk", deleted: false }
];

// Route to get all active users (users that are not deleted)
app.get('/users', (req, res) => {
  const activeUsers = users.filter(u => !u.deleted);  // Filter out deleted users
  res.json(activeUsers);  // Return the list of active users as JSON
});

// Route to get all users, including deleted ones
app.get('/users/all', (req, res) => {
  res.json(users);  // Return all users (including deleted) as JSON
});

// Route to get a user by their ID, only for active users
app.get('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);  // Parse the user ID from the URL parameter
  const user = users.find(u => u.id === userId && !u.deleted);  // Find the active user by ID
  if (user) {
    res.json(user);  // If found, return the user data
  } else {
    res.status(404).json({ message: "User not found" });  // If not found, return a 404 error
  }
});

// Route to create a new user
app.post('/users', (req, res) => {
  const newUser = {
    id: users.length + 1,  // Generate a new ID for the user
    name: req.body.name,  // Get the name from the request body
    age: req.body.age,    // Get the age from the request body
    city: req.body.city,  // Get the city from the request body
    deleted: false        // New users are not deleted by default
  };
  users.push(newUser);  // Add the new user to the users array
  res.status(201).json(newUser);  // Return the created user with a 201 (Created) status
});

// Route to update a user's information (only for active users)
app.put('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);  // Parse the user ID from the URL
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);  // Find the user by ID
  if (userIndex !== -1) {
    users[userIndex] = { ...users[userIndex], ...req.body };  // Update the user with new data
    res.json(users[userIndex]);  // Return the updated user data
  } else {
    res.status(404).json({ message: "User not found" });  // Return a 404 error if user not found
  }
});

// Route to partially update a user's information (only for active users)
app.patch('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);  // Parse the user ID from the URL
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);  // Find the user by ID
  if (userIndex !== -1) {
    users[userIndex] = { ...users[userIndex], ...req.body };  // Partially update the user data
    res.json(users[userIndex]);  // Return the updated user data
  } else {
    res.status(404).json({ message: "User not found" });  // Return a 404 error if user not found
  }
});

// Route to soft delete a user (mark as deleted without removing from the database)
app.delete('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);  // Parse the user ID from the URL
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);  // Find the active user by ID
  if (userIndex !== -1) {
    users[userIndex].deleted = true;  // Mark the user as deleted (soft delete)
    res.status(204).send();  // Respond with a 204 (No Content) status
  } else {
    res.status(404).json({ message: "User not found" });  // Return a 404 error if user not found
  }
});

// Route to reset the API state (restore the original list of users)
app.post('/reset', (req, res) => {
  users = [  // Reset the users array to its original state
    { id: 1, name: "Jan Kowalski", age: 30, city: "Warszawa", deleted: false },
    { id: 2, name: "Anna Nowak", age: 25, city: "Kraków", deleted: false },
    { id: 3, name: "Piotr Wiśniewski", age: 35, city: "Warszawa", deleted: false },
    { id: 4, name: "Maria Kowalczyk", age: 28, city: "Gdańsk", deleted: false }
  ];
  res.status(200).json({ message: "REST API state reset" });  // Respond with a success message
});

// Set the port for the server to listen on
const PORT = 3000;
// Start the server and log a message when it's running
app.listen(PORT, () => {
  console.log(`REST API is running on http://localhost:${PORT}`);
});
