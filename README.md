# Bookstore API

A simple RESTful API for managing books in a bookstore. This API allows users to create, read, update, and delete books stored in a MongoDB database.

---

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
   ```bash
   git clone 
   cd bookstore-api

2. **Create VM**:
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependies** :
pip install -r requirements.txt

4. **Setu Up Env Var:**
MONGO_URI=mongodb://your_mongo_connection_string

5. **Run application** :
python app.py
