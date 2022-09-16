def knight_single_move(input_string):
    x1, y1, x2, y2 = [int(x) for x in input_string.split()]
    vertical = abs(x1 - x2) == 1 and abs(y1 - y2) == 2
    horizontal = abs(x1 - x2) == 2 and abs(y1 - y2) == 1
    if vertical or horizontal:
        return True
    return False
