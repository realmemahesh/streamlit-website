import psycopg2
import bcrypt

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="auth",
        user="postgres",
        password="admin123"
    )

def validate_user(username, password):
    conn = connect_db()
    cursor = conn.cursor() # connection object

    cursor.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    if result:
        hashed_password = result[0]
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8')):
            return True
    return False