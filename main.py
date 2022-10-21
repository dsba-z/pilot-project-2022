import importlib
import inspect
import os
from inspect import getmembers
import argparse
import sys
from src.util import input_int

functions_list = [
    {"prompt": "Exit", "function": exit},
]


def run_function(function_data, task_input):
    answer = function_data["function"](task_input)
    print(f"""Answer:

    {answer}
    """)


modules = []
workshops_directory = os.path.join("src", "workshops")
for path, directory, module in os.walk(workshops_directory):
    for cur in module:
        if "__init__" in cur:
            break
        if ".pyc" in cur:
            break
        with open(os.path.join(workshops_directory, cur), encoding='utf-8') as f:
            if "input()" in f.read():
                break

        workshop_dir_import = workshops_directory.replace("/", ".")
        module = importlib.import_module(workshop_dir_import + "." + cur.replace(".py", ""))
        for func in [i[1] for i in getmembers(module, inspect.isfunction)]:
            docstring = inspect.getdoc(func)
            if docstring is not None:
                doc_first_line = docstring.split("\n", maxsplit=1)[0]
                functions_list.append({"prompt": doc_first_line, "function": func})


def print_greeting(functions):
    print("Choose option:")
    for i, entry in enumerate(functions):
        print(f"{i}. {entry['prompt']}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--problem", type=int, help="Problem number")
    parser.add_argument("--input", type=str, help="Input for problem")
    args = parser.parse_args()
    if args.problem is not None and args.input is not None:
        print(f'> Solving problem "{functions_list[args.problem]["prompt"]}"')
        print(f'> Input is: {args.input}')
        run_function(functions_list[args.problem], args.input)
    else:
        while True:
            print_greeting(functions_list)
            user_input = input_int(start=0, end=len(functions_list) - 1)
            if user_input == 0:
                sys.exit()
                break
            task_input = input("Enter input for the task:\n")
            run_function(functions_list[user_input], task_input)


if __name__ == "__main__":
    main()
