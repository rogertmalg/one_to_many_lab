from flask import Flask, render_template, request, redirect, Blueprint
from models.book import Book
from repositories import book_repository, author_repository

book_blueprint = Blueprint("books", __name__)

@book_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)

@book_blueprint.route("/books/<id>/delete", methods = ["POST"])
def delete_book(id):
    book_repository.delete(id)
    return redirect("/books")