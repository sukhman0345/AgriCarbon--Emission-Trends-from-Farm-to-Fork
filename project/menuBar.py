import streamlit as st
from streamlit_option_menu import option_menu
from about import show_about
from visualization import show_visualization


# for horizontal menu
selected = option_menu(
        menu_title="Co2 Emission",
        options=["About", "Visualization", "Query"],
        icons=["house", "search", "patch-question-fill"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )

# Page Content Based on Selection
if selected == "About":
    show_about()


if selected == "Visualization":
    show_visualization()

if selected == "Query":
    st.title("You are in Query")