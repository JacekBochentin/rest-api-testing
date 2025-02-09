const express = require('express');
const app = express();

app.use(express.json());

// Initial list of users
let users = [
  { id: 1, name: "Jan Kowalski", age: 30, city: "Warszawa", deleted: false },
  { id: 2, name: "Anna Nowak", age: 25, city: "Kraków", deleted: false },
  { id: 3, name: "Piotr Wiśniewski", age: 35, city: "Warszawa", deleted: false },
  { id: 4, name: "Maria Kowalczyk", age: 28, city: "Gdańsk", deleted: false }
];

// Get all active users
app.get('/users', (req, res) => {
  const activeUsers = users.filter(u => !u.deleted);
  res.json(activeUsers);
});

// Get user by ID (only active users)
app.get('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const user = users.find(u => u.id === userId && !u.deleted);
  if (user) {
    res.json(user);
  } else {
    res.status(404).json({ message: "User not found" });
  }
});

// Create a new user
app.post('/users', (req, res) => {
  const newUser = {
    id: users.length + 1,
    name: req.body.name,
    age: req.body.age,
    city: req.body.city,
    deleted: false
  };
  users.push(newUser);
  res.status(201).json(newUser);
});

// Update user (only active users)
app.put('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);
  if (userIndex !== -1) {
    users[userIndex] = { ...users[userIndex], ...req.body };
    res.json(users[userIndex]);
  } else {
    res.status(404).json({ message: "User not found" });
  }
});

// Partially update user (only active users)
app.patch('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);
  if (userIndex !== -1) {
    users[userIndex] = { ...users[userIndex], ...req.body };
    res.json(users[userIndex]);
  } else {
    res.status(404).json({ message: "User not found" });
  }
});

// Soft delete user
app.delete('/users/:id', (req, res) => {
  const userId = parseInt(req.params.id);
  const userIndex = users.findIndex(u => u.id === userId && !u.deleted);
  if (userIndex !== -1) {
    users[userIndex].deleted = true;  // Mark user as deleted
    res.status(204).send();
  } else {
    res.status(404).json({ message: "User not found" });
  }
});

// Get all users (including deleted)
app.get('/users/all', (req, res) => {
  res.json(users);
});

// Reset REST API state
app.post('/reset', (req, res) => {
  users = [
    { id: 1, name: "Jan Kowalski", age: 30, city: "Warszawa", deleted: false },
    { id: 2, name: "Anna Nowak", age: 25, city: "Kraków", deleted: false },
    { id: 3, name: "Piotr Wiśniewski", age: 35, city: "Warszawa", deleted: false },
    { id: 4, name: "Maria Kowalczyk", age: 28, city: "Gdańsk", deleted: false }
  ];
  res.status(200).json({ message: "REST API state reset" });
});

const PORT = 3000;
app.listen(PORT, () => {
  console.log(`REST API is running on http://localhost:${PORT}`);
});