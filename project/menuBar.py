import streamlit as st
from streamlit_option_menu import option_menu
from about import show_about
from visualization import show_visualization
from touch import get_in_touch
from signin import signin
from signup import signup

# Initialize session state
if "user" not in st.session_state:
    st.session_state.user = None

# If user is not logged in
if st.session_state.user is None:
    auth_option = st.sidebar.selectbox("Login / Signup", ["Sign In", "Sign Up"])
    if auth_option == "Sign In":
        signin()
    elif auth_option == "Sign Up":
        signup()

# If user is logged in
else:
    selected = option_menu(
        menu_title="Co2 Emission",
        options=["About", "Visualization", "Get In Touch"],
        icons=["house", "search", "patch-question-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

    # Page Content Based on Selection
    if selected == "About":
        show_about()

    elif selected == "Visualization":
        show_visualization()

    elif selected == "Get In Touch":
        get_in_touch()
