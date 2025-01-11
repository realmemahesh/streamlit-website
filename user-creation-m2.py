import streamlit as st
import bcrypt
import psycopg2

def connect_db():
    return psycopg2.connect(
        host="localhost",
        database="auth",
        user="postgres",
        password="admin123"
    )

def insert_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    # Encrypt the password
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed.decode('utf-8')))
        conn.commit()
        return True
    except psycopg2.Error as e:
        print (e)
        conn.rollback()
        return False
    finally:
        cursor.close()
        conn.close()

# Streamlit UI for Sign-Up
st.title("Sign Up - Create an Account")

username = st.text_input("Username")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

if password and confirm_password and password != confirm_password:
    st.error("Passwords do not match!")

if st.button("Sign Up"):
    if username and password and confirm_password == password:
        if insert_user(username, password):
            st.success("Account created successfully!")
        else:
            st.error("Error creating account. Please try again.")
    else:
        st.error("Please fill all fields correctly.")
