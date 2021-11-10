import pdb
import os

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

os.system('psql -d library -f db/library.sql')

author_1 = Author("Dan Brown")
author_repository.save(author_1)

author_2 = Author("J R R Tolkien")
author_repository.save(author_2)

book_01 = Book("DaVinci Code", author_1, 300)
book_repository.save(book_01)

book_02 = Book("Inferno", author_1, 450)
book_repository.save(book_02)

book_03 = Book("Lord of the Rings", author_2, 500)
book_repository.save(book_03)


pdb.set_trace()