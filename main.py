from workshops.numeral_systems import convert
from workshops.zoom_link import zoom

greeting = '''Choose option:
1. Convert number from any base to any base.
2. Solve the knight move problem
3. Extract ID from Zoom link
0. Exit
'''


def pass_input(func):
    task_input = input("Provide input for the task: \n")
    print("\nAnswer:\n")
    print(func(task_input), "\n")


while True:
    user_input = input(greeting)
    if user_input == '1':
        pass_input(convert)
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass_input(zoom)
    elif user_input == '0':
        break
