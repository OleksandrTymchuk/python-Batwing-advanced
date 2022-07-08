class BookDB:
    books = [{"name": "The Witcher", "author": "Andrzej Sapkowski", "genre": "Fantasy", "id": 1}]

    def get_all(self):
        return self.books

    def retrieve(self, id):
        try:
            book_id = int(id)
            for book in self.books:
                if book["id"] == book_id:
                    return book
                else:
                    return 'Sad', 400

        except Exception:
            result = ("Wrong data (You must use only numbers for books id's)", 400)
            return result

    def add(self, name, author, genre, id):
        exist = False

        for book in self.books:
            if id == book['id']:
                exist = True

        if not exist:
            book = {
                "name": name,
                "author": author,
                "genre": genre,
                "id": self.books[-1]['id'] + 1
            }
            self.books.append(book)
            return book

    def update(self, name, author, genre, id):
        int_id = int(id)
        for book in self.books:
            if book["id"] == int_id:
                book["author"] = author
                book["genre"] = genre
                book['name'] = name
                return book
        return "Wrong data (You must use only numbers for books id's)", 400

    def delete(self, id):
        self.books = [book for book in self.books if book["id"] != id]
