from db.run_sql import run_sql
from models.author import Author
from models.book import Book

def select_all():
    authors = []

    sql = "SELECT * FROM authors"
    results = run_sql(sql)

    for row in results:
        author = Author(row['name'], row['id'])
        authors.append(author)
    return authors 
 
def save(author):
    sql = "INSERT INTO authors(name) VALUES (%s) RETURNING *"
    values = [author.name]
    result = run_sql(sql, values)
    id = result[0]['id']
    author.id = id
    return author
