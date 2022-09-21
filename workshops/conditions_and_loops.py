def can_knight_move(input_string):
    x1, y1, x2, y2 = map(int, input_string.split())
    if ((abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or
            (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)):
        return True
    else:
        return False

def solve_the_knight_move_problem(input_string):
    if can_knight_move(input_string):
        return "Yes, it can"
    else:
        return "No, it cannot"
