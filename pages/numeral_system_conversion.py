import streamlit as st
from src.workshops.numeral_systems import convert_internal

st.title('Numeral systems')

st.text('Convert a number from any numeral system to any other (up to 36)')

init_number_text = st.text_input("Number")
from_base = st.number_input("Initial base", min_value=2, max_value=36)
to_base = st.number_input("Target base", min_value=2, max_value=36)

try:
    result = convert_internal(init_number_text, from_base, to_base)
    result_text = f"Output is {result}"
except ValueError:
    result_text = "Incorrect number for this base"

result = st.text(result_text)
