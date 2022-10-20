import streamlit as st
from src.workshops.regexp import list_isbn
from src.workshops.regexp import list_urls

st.title("Tasks related to regular expressions")

st.subheader("Find ISBN IDs in a text string")

example_isbn = "Example text that contains some numbers like this 978-5-8243-1727-5."
text_for_isbn = st.text_area("Enter text with ISBNs", value=example_isbn)
isbn_result = list_isbn(text_for_isbn)
st.write(isbn_result)


st.subheader("Find URLs in a text string")

example_url = """hse.ru
www.hse.ru
https://hse.ru
python.exe
http://user:password@domain.com/
"""
text_for_url = st.text_area("Enter text with URLs", value=example_url)
url_result = list_urls(text_for_url)
st.write(url_result)
