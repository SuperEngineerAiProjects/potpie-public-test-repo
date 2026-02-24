import streamlit as st

# Set the title of the app
st.title('Simple Streamlit App')

# Add a text input widget
author_name = st.text_input('Enter your name:', '')

# Display a welcome message if a name is entered
if author_name:
    st.subheader(f'Hello, {author_name}! Welcome to this simple Streamlit app.')

# Add a slider widget
gradient = st.slider('Pick a gradient:', 0, 100, 50)

# Display the current value of the slider
st.write(f'Current gradient value: {gradient}')
