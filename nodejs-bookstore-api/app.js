// File: app.js
const express = require('express');
const app = express();
app.use(express.json());

let books = [{ id: 1, title: "DevOps Handbook" }];

app.get('/books', (req, res) => {
  res.json(books);
});

app.post('/books', (req, res) => {
  const book = { id: books.length + 1, title: req.body.title };
  books.push(book);
  res.json(book);
});

app.listen(3000, () => console.log("Bookstore API running on port 3000"));
