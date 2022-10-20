def can_knight_move(x1, y1, x2, y2):
    if ((abs(x1 - x2) == 1 and abs(y1 - y2) == 2) or
            (abs(x1 - x2) == 2 and abs(y1 - y2) == 1)):
        return True
    return False


def solve_the_knight_move_problem(input_string):
    """Solve the knight move problem."""
    if can_knight_move(input_string):
        return "Yes, it can"
    return "No, it cannot"
