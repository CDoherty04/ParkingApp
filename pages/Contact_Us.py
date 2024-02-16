import streamlit as st

with st.form(key="form"):
    email = st.text_input("Email")
    topic = st.selectbox("Select a topic", index=None, options=["Comment", "Question", "Other"])
    message = st.text_area("Message", placeholder="Enter your message here...")
    button = st.form_submit_button("Submit")

    message = f"""\
Subject: Company Website inquiry about {topic}

{message}

From: {email}
"""

    if button:
        st.info("Email sent successfully!")
