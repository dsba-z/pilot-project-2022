from workshops.numeral_systems import convert
from workshops.chess import knight_single_move

greeting = '''Choose option:
1. Convert number from any base to any base.
2. Solve the knight move problem
3. Exit
'''


def pass_input(func):
    task_input = input("Provide input for the task: \n")
    print("Answer:\n")
    print(func(task_input))


while True:
    user_input = input(greeting)
    if user_input == '1':
        pass_input(convert)
    elif user_input == '2':
        pass_input(knight_single_move)
    elif user_input == '3':
        break
