import streamlit as st
from src.workshops.code_reading import task1, task2


st.title("Workshop 13 tasks")
st.subheader("Fetch weather data")
city = st.text_input('City')
st.write(task1(city))

st.subheader("Get featires of a github repo")
repo = st.text_input('Repo Name')
st.write(task2(repo))
