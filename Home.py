import streamlit as st

st.set_page_config(page_title="Home", page_icon="🏠")

st.title("Welcome to LCY")
st.write(
    "This is the Home page for the Streamlit multipage app. "
    "Click the button below to open the App page."
)

if st.button("Go to App"):
    st.switch_page("pages/app.py")
