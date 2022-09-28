import importlib
import inspect
import os
from inspect import getmembers

from src.util import input_int

functions_list = [
    {"prompt": "Exit", "function": exit},
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


modules = []
workshops_directory = 'workshops'

for path, directory, module in os.walk(workshops_directory):
    for cur in module:
        if '__init__' in cur:
            break
        if '.pyc' in cur:
            break
        if 'input()' in open(os.path.join(workshops_directory, cur)).read():
            break

        module = importlib.import_module(workshops_directory + '.' + cur.replace('.py', ''))
        for func in [i[1] for i in getmembers(module, inspect.isfunction)]:
            docstring = inspect.getdoc(func)
            if docstring is not None:
                doc_first_line = docstring.split('\n')[0]
                functions_list.append({"prompt": doc_first_line, "function": func})


def print_greeting(functions):
    print("Choose option:")
    for i, entry in enumerate(functions):
        print(f"{i}. {entry['prompt']}")


while True:
    print_greeting(functions_list)
    user_input = input_int(start=0, end=len(functions_list) - 1)
    if user_input == 0:
        exit()
        break
    run_function(functions_list[user_input])
