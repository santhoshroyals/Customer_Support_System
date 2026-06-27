import sqlite3

DATABASE = "database/memory.db"


def initialize_database():
    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id TEXT,
            customer_name TEXT,
            query TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_conversation(customer_id, customer_name, query):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO conversations(customer_id, customer_name, query)
        VALUES (?, ?, ?)
    """, (customer_id, customer_name, query))

    conn.commit()
    conn.close()


def get_previous_issue(customer_id):

    conn = sqlite3.connect(DATABASE)

    cursor = conn.cursor()

    cursor.execute("""
        SELECT query
        FROM conversations
        WHERE customer_id = ?
        ORDER BY id DESC
    """, (customer_id,))

    rows = cursor.fetchall()

    conn.close()

    for row in rows:

        # Ignore memory questions
        if "previous support issue" not in row[0].lower():

            return row[0]

    return "No previous support issue found."