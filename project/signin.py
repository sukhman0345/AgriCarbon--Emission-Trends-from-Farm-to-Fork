# project/signin.py

import streamlit as st
import requests
import json

def signin():
    st.title("Sign In")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        try:
            api_key = "AIzaSyDo3JD18lExhQYiLC53VvMEWP_U8wMwrRQ"  # replace with your real key
            url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"

            payload = json.dumps({
                "email": email,
                "password": password,
                "returnSecureToken": True
            })

            res = requests.post(url, data=payload)
            if res.status_code == 200:
                result = res.json()
                st.success("Logged in successfully!")

                # Save user login in session state
                st.session_state.user = result["email"]

                # Force rerun so menuBar detects login
                st.rerun()

            else:
                st.error("Invalid email or password.")
        except Exception as e:
            st.error(f"Error: {e}")
