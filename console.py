import pdb
import os

from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

os.system('psql -d library -f db/library.sql')

author_1 = Author("Dani Brown")
author_repository.save(author_1)
author_2 = Author("J R R Tolkien")
author_repository.save(author_2)

author_repository.select_all()

author_1.name = "Dan Brown"
author_repository.update(author_1)

author = author_repository.select(1)
print(author.__dict__)


pdb.set_trace()