import streamlit as st
from src.workshops.real_numbers_and_strings import interest_rate
from src.workshops.conditions_and_loops import can_knight_move
from src.workshops.sublists import get_sublists
from src.workshops.zoom_link import zoom

st.title("Small tasks similar to the ones from the contest")

st.subheader("Calculate interest rate")

rate = st.number_input("Interest rate in percent", min_value=0)
rubles = st.number_input("Rubles", min_value=0)
kopecks = st.number_input("Kopecks", min_value=0)

final_rub, final_kop = interest_rate(rate, rubles, kopecks)

st.write(f"Final sum is {final_rub} rubles and {final_kop} kopecks")

# Knight's move
st.subheader("Knight's move")

x1 = st.number_input("X1", min_value=1, max_value=8)
y1 = st.number_input("Y1", min_value=1, max_value=8)
x2 = st.number_input("X2", min_value=1, max_value=8)
y2 = st.number_input("Y2", min_value=1, max_value=8)

can_jump = can_knight_move(x1, y1, x2, y2)

if can_jump:
    knight_result = "Yes, the knight can make this move"
else:
    knight_result = "No, the knight cannot make this move"

st.write(knight_result)

# All sublists of a list
st.subheader("All sublists of a list")


word_list = st.text_input("Enter a list of words separated by spaces")
word_list = word_list.split()

word_list_sublists = get_sublists(word_list)
st.write(str(word_list_sublists))


# Extract ID from a Zoom link
st.subheader("Extract ID from a Zoom link")

initial_link = "https://us04web.zoom.us/j/123456789/pwd=bkN3djZmYlZ5MStFMWdqdmphSGFVdz09"
link = st.text_input("Enter a link", value=initial_link)

try:
    link_id = zoom(link)
except IndexError:
    link_id = "Invalid link"
st.write(link_id)
