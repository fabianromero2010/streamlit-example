import streamlit as st

# Text files

text_contents = '''
Foo, Bar
123, 456
789, 000
'''

# Different ways to use the API


st.download_button('Download CSV', text_contents)  # Defaults to 'text/plain'



