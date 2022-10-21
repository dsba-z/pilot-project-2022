import streamlit as st
from src.workshops.code_reading_requests import main

st.title('Requests JSON parsing')

st.text('Get current weather in a city')

city_name = st.text_input("City name")

try:
    result_text = main(city_name)
except Exception as e:
    result_text = str(e)

result = st.text(result_text)
