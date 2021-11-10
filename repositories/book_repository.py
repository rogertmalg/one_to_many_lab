from db.run_sql import run_sql
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repository 

def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['pages'], row['id'])
        books.append(book)
    return books

def save(book):
    sql = "INSERT INTO books (title, author_id, pages) VALUES (%s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.pages]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book