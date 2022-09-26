from workshops.numeral_systems import convert
from workshops.conditions_and_loops import solve_the_knight_move_problem
from workshops.real_numbers_and_strings import interest_rate_wrapper
from workshops.regexp import list_isbn_from_file, list_urls_from_file


greeting = '''Choose option:
1. Convert number from any base to any base.
2. Solve the knight move problem
3. Solve interest rate problem
4. Find all ISBN codes in a file
5. Find all URL's in a file
6. Exit
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
        pass_input(solve_the_knight_move_problem)
    elif user_input == '3':
        pass_input(interest_rate_wrapper)
    elif user_input == '4':
        pass_input(list_isbn_from_file)
    elif user_input == '5':
        pass_input(list_urls_from_file)
    elif user_input == '6':
        break
