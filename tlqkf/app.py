# app.py
import streamlit as st
import os

# Set a wide layout for the app
st.set_page_config(layout="wide")

# Path to the HTML file
# The path is now set to 'team_creator.html' within the current directory.
html_file_path = os.path.join(os.path.dirname(__file__), "team_creator.html")

# Check if the HTML file exists
if not os.path.exists(html_file_path):
    st.error(f"Error: The HTML file was not found at {html_file_path}")
    st.stop()

# Read the HTML content from the file
try:
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Render the HTML content
    st.html(html_content)

except Exception as e:
    st.error(f"An error occurred while reading the HTML file: {e}")
    
