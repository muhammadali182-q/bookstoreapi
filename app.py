from flask import Flask, request, jsonify
from flask_restful import Api
from controllers.book_controller import BookList, BookCreate, BookDetail
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
api = Api(app)

# Register routes
api.add_resource(BookList, '/books')
api.add_resource(BookCreate, '/books')
api.add_resource(BookDetail, '/books/<string:id>')

if __name__ == "__main__":
    app.run(debug=True)
