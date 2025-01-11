import streamlit as st
from db import validate_user #importing from local db module

st.set_page_config(page_title="Strealit Auth App", layout="centered")

st.title("User Authentication")

#Input fields for login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"): # return true if button is clicked
    if validate_user(username, password): # validate_user is a function from db.py
        st.success("Login Sucessfull !") 
    else:
        st.error("Invalid credentials. Please try again.")

st.write("Don't have an account?")
if st.button("Sign Up"):
    #st.markdown("<a href='http://localhost:8502' target='_blank'>Sign Up</a>", unsafe_allow_html=True)
    st.markdown("""<meta http-equiv="refresh" content="0; url=http://localhost:8502/">""",unsafe_allow_html=True)