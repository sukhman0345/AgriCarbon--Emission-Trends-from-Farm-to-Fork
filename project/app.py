import streamlit as st
from signin import signin
from signup import signup
from menuBar import main_app  #  dashboard app

def main():
    if st.session_state.get('user'):
        main_app()
    else:
        st.sidebar.title("Login/Signup")
        auth_choice = st.sidebar.radio("", ["Login", "Sign Up"])

        if auth_choice == "Login":
            signin()
        else:
            signup()

if __name__ == "__main__":
    main()
