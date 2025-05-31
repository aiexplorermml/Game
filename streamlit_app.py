import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="2048 Game",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Read the HTML file content
html = Path("2048.html").read_text()

# Display the HTML using Streamlit components
st.components.v1.html(html, width=400, height=700, scrolling=True)
