import streamlit as st
from datetime import datetime
import sqlite3

def get_in_touch():
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
        c = conn.cursor() # c is for cursor

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

        st.success("Thanks for your feedback! It's been recorded.")