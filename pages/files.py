import streamlit as st
from src.workshops.files import task1


st.title("Workshop 12 tasks")

st.subheader("Tree-alike structure of the directory")
d = st.text_input('Directory')
st.text(task1(d))
