import sqlite3
import pytest

@pytest.fixture
def db_connection():
    conn = sqlite3.connect(':memory:')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE carrito (
            id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            product_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            price REAL NOT NULL,
            description TEXT,
            category TEXT,
            image TEXT
        )
    ''')

    conn.commit()
    yield conn
    conn.close()