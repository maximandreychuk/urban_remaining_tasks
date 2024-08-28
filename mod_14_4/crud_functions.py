import sqlite3

conn = sqlite3.connect('products.db')
cursor = conn.cursor()


def initiate_db():
    with conn:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products_table (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                price INTEGER NOT NULL
            );
        """)


def get_all_products():
    cursor.execute(
        'SELECT products_table.id, products_table.title, products_table.description, products_table.price FROM products_table')
    res = cursor.fetchall()
    return res

def add_values():
    cursor.execute(
        'INSERT INTO products_table (title, description, price) VALUES("Green", "Tea, Gras", "12")')
    cursor.execute(
        'INSERT INTO products_table (title, description, price) VALUES("Red", "Flag, Chili", "48")')
    cursor.execute(
        'INSERT INTO products_table (title, description, price) VALUES("Blue", "Horizont, Jeans", "34")')
    cursor.execute(
        'INSERT INTO products_table (title, description, price) VALUES("Yellow", "Sun", "5003")')
    conn.commit()


if __name__ == "__main__":
    initiate_db()
    add_values()