import streamlit as st
import time
import os
import json
from streamlit_lottie import st_lottie
from signin import signin
from signup import signup
from menuBar import main_app  #  dashboard app

# Function to load the Lottie JSON
def load_lottie_animation(path):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, path)
    with open(file_path, "r") as file:
        return json.load(file)

   
def splash_screen():
    lottie_data = load_lottie_animation("splash_screen.json")
    st_lottie(lottie_data, speed=3, loop=True, quality="high")
    st.markdown("<h2 style='text-align:center;'>Loading The Carbonivore...</h2>", unsafe_allow_html=True)
    time.sleep(2)
    st.session_state.splash_done = True
    st.rerun()
   

def main():
    if "splash_done" not in st.session_state:
        splash_screen() # Show splash on first load

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
