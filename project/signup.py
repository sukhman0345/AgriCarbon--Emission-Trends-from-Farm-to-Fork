import streamlit as st
from firebase_admin import auth
import firebase_config 

def signup():
  st.title("Sign Up")

  email = st.text_input("Email")
  password = st.text_input("Password", type="password")

  if st.button("Register"):
    try:
      user= auth.create_user(email=email, password=password)
      st.success("Account created successfully")
      st.info(f"User ID: {user.uid}")
    except Exception as e:
      st.error(f"Error:{e}") 