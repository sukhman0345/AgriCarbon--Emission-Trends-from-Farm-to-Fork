import streamlit as st
import time
import json
import requests
from streamlit_lottie import st_lottie
from signin import signin
from signup import signup
from menuBar import main_app

# Load Lottie animation from URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Splash screen
def splash_screen():
    lottie_data = load_lottieurl(
        "https://lottie.host/a88b4f1e-bc10-4d78-89bc-39b6b6fd7923/a9d54LJf0Z.json"
    )  # Replace with your Lottie animation link
    if lottie_data:
        st_lottie(lottie_data, speed=1, loop=True, quality="high")
    st.markdown("<h2 style='text-align:center;'>Loading The Carbonivore...</h2>", unsafe_allow_html=True)
    time.sleep(1)
    st.session_state.splash_done = True
    st.rerun()

# Main app logic
def main():
    if "splash_done" not in st.session_state:
        splash_screen()
    if st.session_state.get('user'):
        main_app()
    else:
        st.sidebar.title("Signin/Signup")
        auth_choice = st.sidebar.radio("Select", ["Sign In", "Sign Up"])
        if auth_choice == "Sign In":
            signin()
        else:
            signup()

if __name__ == "__main__":
    main()
