from workshops.numeral_systems import convert
from workshops.conditions_and_loops import solve_the_knight_move_problem
from workshops.real_numbers_and_strings import interest_rate_wrapper
from workshops.regexp import list_isbn_from_file, list_urls_from_file
from workshops.zoom_link import zoom
from workshops.strings_code_style import text_filter_wrapper
from src.util import input_int

functions = [
    {"prompt": "Exit", "function": None},
    {"prompt": "Convert number from any base to any base.", "function": convert},
    {"prompt": "Solve the knight move problem.", "function": solve_the_knight_move_problem},
    {"prompt": "Calculate interest problem.", "function": interest_rate_wrapper},
    {"prompt": "Extract ID from Zoom link.", "function": zoom},
    {"prompt": "Filter text from the link.", "function": text_filter_wrapper},
    {"prompt": "Find all ISBN codes in a file.", "function": list_isbn_from_file},
    {"prompt": "Find all URL's in a file.", "function": list_urls_from_file},
]


def pass_input(func):
    task_input = input("\nProvide input for the task: \n")
    print("\nAnswer:\n")
    print(func(task_input), "\n")


def run_function(function_data):
    task_input = input("Enter input for the task:\n")
    answer = function_data["function"](task_input)
    print(f"""
    Answer:

    {answer}
    """)


def print_greeting(functions):
    print("Choose option:")
    for i, entry in enumerate(functions):
        print(f"{i}. {entry['prompt']}")


while True:
    print_greeting(functions)
    user_input = input_int(start=0, end=len(functions) - 1)
    if user_input == "0":
        break
    run_function(functions[user_input])
