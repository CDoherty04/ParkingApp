import streamlit as st

# Keeps the page from being too narrowly restricted
st.set_page_config(layout="wide", page_title="Parking Webapp",
                   menu_items={
                       'Get Help': 'mailto:charlieedoherty@gmail.com',
                       'Report a bug': "mailto:charlieedoherty@gmail.com",
                       'About': "# This is a header. This is an *extremely* cool app!"})

# Text displayed at the top of the page
st.title("Welcome to Our Parking App!")
content = ("ChatGPT blob: Innovation meets excellence in every endeavor. As a pioneering force in our industry, "
           "we are dedicated to delivering unparalleled solutions that redefine standards and exceed expectations. "
           "With a relentless commitment to quality, integrity, and client satisfaction, we empower businesses to "
           "thrive in dynamic environments. Backed by a team of seasoned experts and fueled by a passion for progress, "
           "we harness the latest technologies and strategic insights to drive transformative outcomes. Explore our "
           "comprehensive suite of services and discover how we can catalyze your success today.")
st.write(content)
st.markdown("***")  # Break line

col1, col2, col3, col4, col5 = st.columns(5)

with col2:
    st.button("Pay", key="Pay", use_container_width=True)
with col3:
    st.button("Login", key="Login", use_container_width=True)
with col4:
    st.button("Logout", key="Logout", use_container_width=True)

st.markdown("***")  # Break line

with st.expander("FAQ"):
    st.write("""
    1. How do I use this website?\n
            By clicking on different buttons.
            
    2. When can I make a payment?\n
            Whenever you want to.
        
    3. How was this website built?\n
            Hard work and dedication.
    """)
