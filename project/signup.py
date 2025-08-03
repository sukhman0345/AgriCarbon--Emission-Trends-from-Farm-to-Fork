import streamlit as st
from firebase_config import auth

def signup():
  st.title("📝 Sign Up")
  email = st.text_input("📧 Email")
  password = st.text_input("🔒 Password", type="password")
  confirm = st.text_input("🔁 Confirm Password", type="password")

  if st.button("🧷 Create Account"):
    if password != confirm:
      st.error(" Passwords do not match.")
    else:
      try:
        auth.create_user_with_email_and_password(email, password)
        st.success("🎉 Account created successfully. Please sign in.")
      except Exception as e:
        st.error(f" Error: {e}")
