import sqlite3


class DBHelper:

    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)

    def create_tables(self):

        cursor = self.conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT,
                email TEXT
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                customer_id INTEGER,
                total_amount REAL,
                status TEXT
            )
        """)

        self.conn.commit()

    def insert_customer(self, customer_id, name, email):

        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO customers (id, name, email)
            VALUES (?, ?, ?)
        """, (customer_id, name, email))

        self.conn.commit()

    def insert_order(
        self,
        order_id,
        customer_id,
        total_amount,
        status
    ):

        cursor = self.conn.cursor()

        cursor.execute("""
            INSERT INTO orders
            (id, customer_id, total_amount, status)
            VALUES (?, ?, ?, ?)
        """, (
            order_id,
            customer_id,
            total_amount,
            status
        ))

        self.conn.commit()

    def get_order_by_id(self, order_id):

        cursor = self.conn.cursor()

        cursor.execute(
            "SELECT * FROM orders WHERE id = ?",
            (order_id,)
        )

        return cursor.fetchone()

    def close(self):
        self.conn.close()