from pymongo import MongoClient
import os

class Database:
    def __init__(self):
        self.client = MongoClient(os.getenv("MONGO_URI"))
        self.db = self.client['bookstore']
        self.books_collection = self.db.books

    def get_all_books(self):
        return list(self.books_collection.find())

    def get_book_by_id(self, book_id):
        return self.books_collection.find_one({"_id": book_id})

    def create_book(self, book_data):
        self.books_collection.insert_one(book_data)

    def update_book(self, book_id, update_data):
        self.books_collection.update_one({"_id": book_id}, {"$set": update_data})

    def delete_book(self, book_id):
        self.books_collection.delete_one({"_id": book_id})
