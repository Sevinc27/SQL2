import sqlite3


connection = sqlite3.connect("library.db")
cursor = connection.cursor()


def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author_id INTEGER,
            publisher TEXT,
            pages INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id)
        )
    """)


create_tables()


def add_author(name):
    cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
    connection.commit()


def add_book(title, author_id, publisher, pages):
    cursor.execute("INSERT INTO books (title, author_id, publisher, pages) VALUES (?, ?, ?, ?)", (title, author_id, publisher, pages))
    connection.commit()


add_author("Orhan Pamuk")
add_author("Elif Şafak")
add_book("Kırmızı Saçlı Kadın", 1, "Yapı Kredi Yayınları", 204)
add_book("Aşk", 2, "Doğan Kitap", 419)


def show_authors():
    cursor.execute("SELECT * FROM authors")
    authors = cursor.fetchall()
    for author in authors:
        print(author)


def show_books():
    cursor.execute("SELECT books.id, books.title, authors.name, books.publisher, books.pages FROM books JOIN authors ON books.author_id = authors.id")
    books = cursor.fetchall()
    for book in books:
        print(book)


show_authors()
show_books()


def update_publisher(old_publisher, new_publisher):
    cursor.execute("UPDATE books SET publisher = ? WHERE publisher = ?", (new_publisher, old_publisher))
    connection.commit()


update_publisher("Doğan Kitap", "Doğan Yayınları")
show_books()


def delete_author(author_id):
    cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
    connection.commit()


def delete_book(book_id):
    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
    connection.commit()


delete_book(1)
show_books()


connection.close()