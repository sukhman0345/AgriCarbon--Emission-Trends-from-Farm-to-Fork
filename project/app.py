import streamlit as st
import time
import requests
from streamlit_lottie import st_lottie
from signin import signin
from signup import signup
from menuBar import main_app  # dashboard app

# Function to load Lottie from URL
def load_lottie_url(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        return None
    return response.json()

# Splash screen function
def splash_screen():
    # Use the Lottie JSON URL
    lottie_data = load_lottie_url("https://lottie.host/79ebdf46-b5e6-476e-9c27-7f7bff5cf29a/a3lJp1z6tU.json")
    if lottie_data:
        st_lottie(lottie_data, speed=1, loop=True, quality="high", height=300)
    st.markdown("<h2 style='text-align:center;'>Loading The Carbonivore...</h2>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()

# Main function
def main():
    if "splash_done" not in st.session_state:
        splash_screen()  # Show splash on first load

    if st.session_state.get('user'):
        main_app()
    else:
        st.sidebar.title("Login / Signup")
        auth_choice = st.sidebar.radio("Choose an option:", ["Login", "Sign Up"])

        if auth_choice == "Login":
            signin()
        else:
            signup()

if __name__ == "__main__":
    main()
