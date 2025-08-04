import streamlit as st
from datetime import datetime
import sqlite3

def get_in_touch():
    st.image("https://images.unsplash.com/uploads/141103282695035fa1380/95cdfeef?q=80&w=1430&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", use_container_width=True)
    st.title("Get in touch")

    # User fields
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_input("Your Message")

    # For feedback dropdown
    feedback_type = st.selectbox(
        "Type of Feedback",
        ["Suggestion", "Bug Report", "Compliment", "Question", "Others"]
    )

    if st.button("Submit"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # IST timestamp

        conn = sqlite3.connect("contacts.db")
        c = conn.cursor()  # c is for cursor

        # Create table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS contacts(
                name TEXT,
                email TEXT,
                message TEXT,
                feedback_type TEXT,
                timestamp TEXT
            )
        ''')

        # Insert data
        c.execute("INSERT INTO contacts (name, email, message, feedback_type, timestamp) VALUES(?, ?, ?, ?, ?)",
                  (name, email, message, feedback_type, timestamp))
        conn.commit()
        conn.close()

        # Footer and links
        st.markdown("""
            <p style="text-align: center; color: gray;">
            Made with ❤️ by sukhman.singh.codes
            </p>
        """, unsafe_allow_html=True)


        st.success("Thanks for your feedback! It's been recorded.")
