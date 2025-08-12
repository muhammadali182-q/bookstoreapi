
# Bookstore API

A simple RESTful API for managing books in a bookstore. This API allows users to create, read, update, and delete books stored in a MongoDB database.

## Table of Contents

1. [Technologies Used](#technologies-used)
2. [How to Run Locally](#how-to-run-locally)
3. [Environment Variables](#environment-variables)
4. [API Endpoints](#api-endpoints)
    - [POST /books](#post-books)
    - [GET /books](#get-books)
    - [GET /books/:id](#get-book-by-id)
    - [PUT /books/:id](#put-book-by-id)
    - [DELETE /books/:id](#delete-book-by-id)
5. [Sample Input and Output](#sample-input-and-output)
6. [License](#license)

---

## Technologies Used

- **Python**: Backend programming language
- **Flask**: Web framework for building APIs
- **Flask-RESTful**: Extension for building REST APIs easily
- **Flask-Cors**: To handle Cross-Origin Resource Sharing
- **PyMongo**: MongoDB driver for Python
- **dotenv**: For environment variable management
- **MongoDB**: NoSQL database for storing books data

---

## How to Run Locally

1. **Clone the repository**:
   
   git clone 
   cd bookstore-api


2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root of your project with the following content:

   ```plaintext
   MONGO_URI=mongodb://your_mongo_connection_string
   ```

   Replace `your_mongo_connection_string` with your actual MongoDB URI.

5. **Run the Flask application**:

   ```bash
   python app.py
   ```

   The API will be running at `http://127.0.0.1:5000`.

---

## Environment Variables

The project requires the following environment variable:

* **MONGO\_URI**: MongoDB connection string to connect to your database.

---

## API Endpoints

### `POST /books`

Create a new book.

#### Request:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

#### Response:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

### `GET /books`

Get a list of all books in the bookstore.

#### Response:

```json
[
  {
    "_id": "60f5aaf1f4d1f6b96bdb5c80",
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 20,
    "isbn": "1234567890",
    "publishedDate": "2018-10-16"
  },
  {
    "_id": "60f5aaf1f4d1f6b96bdb5c81",
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "price": 15,
    "isbn": "0987654321",
    "publishedDate": "1988-05-01"
  }
]
```

### `GET /books/:id`

Get a specific book by its ID.

#### Request:

```bash
GET /books/60f5aaf1f4d1f6b96bdb5c80
```

#### Response:

```json
{
  "_id": "60f5aaf1f4d1f6b96bdb5c80",
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

### `PUT /books/:id`

Update the details of an existing book by ID.

#### Request:

```json
{
  "title": "Atomic Habits (Updated)",
  "author": "James Clear",
  "price": 25,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

#### Response:

```json
{
  "title": "Atomic Habits (Updated)",
  "author": "James Clear",
  "price": 25,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

### `DELETE /books/:id`

Delete a book by its ID.

#### Request:

```bash
DELETE /books/60f5aaf1f4d1f6b96bdb5c80
```

#### Response:

```json
{
  "message": "Book deleted"
}
```

---

## Sample Input and Output

### `POST /books`

#### Input:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

#### Output:

```json
{
  "title": "Atomic Habits",
  "author": "James Clear",
  "price": 20,
  "isbn": "1234567890",
  "publishedDate": "2018-10-16"
}
```

### `GET /books`

#### Output:

```json
[
  {
    "_id": "60f5aaf1f4d1f6b96bdb5c80",
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 20,
    "isbn": "1234567890",
    "publishedDate": "2018-10-16"
  },
  {
    "_id": "60f5aaf1f4d1f6b96bdb5c81",
    "title": "The Alchemist",
    "author": "Paulo Coelho",
    "price": 15,
    "isbn": "0987654321",
    "publishedDate": "1988-05-01"
  }
]
```

---

## Author:
This is Made By Muhammad Ali.


