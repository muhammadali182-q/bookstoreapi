from flask_restful import Resource
from flask import request, jsonify
from models.book import Database
from bson.objectid import ObjectId

class BookList(Resource):
    def get(self):
        db = Database()
        books = db.get_all_books()
        for book in books:
            book['_id'] = str(book['_id'])  # Convert _id to string
        return jsonify(books)

class BookCreate(Resource):
    def post(self):
        db = Database()
        data = request.get_json()
        book = {
            "title": data["title"],
            "author": data["author"],
            "price": data["price"],
            "isbn": data["isbn"],
            "publishedDate": data["publishedDate"]
        }
        db.create_book(book)
        return jsonify(book)

class BookDetail(Resource):
    def get(self, id):
        db = Database()
        book = db.get_book_by_id(ObjectId(id))
        if book:
            book['_id'] = str(book['_id'])
            return jsonify(book)
        return {'message': 'Book not found'}, 404

    def put(self, id):
        db = Database()
        data = request.get_json()
        updated_data = {
            "title": data["title"],
            "author": data["author"],
            "price": data["price"],
            "isbn": data["isbn"],
            "publishedDate": data["publishedDate"]
        }
        db.update_book(ObjectId(id), updated_data)
        return jsonify(updated_data)

    def delete(self, id):
        db = Database()
        db.delete_book(ObjectId(id))
        return {'message': 'Book deleted'}, 200
