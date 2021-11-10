import pdb

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author_1 = Author("Dan Brown")
author_repository.save(author_1)
author_2 = Author("J R R Tolkien")
author_repository.save(author_2)

author_repository.select_all()


pdb.set_trace()