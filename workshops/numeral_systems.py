def convert_internal(original_number, from_base=10, to_base=10):
    number = int(original_number, from_base)

    if to_base == 10:
        return str(number)

    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    result = ''
    while number > 0:
        result = alphabet[number % to_base] + result
        number //= to_base
    return result


def convert(input_string):
    """Convert number from any base to any base."""
    number, from_base, to_base = input_string.split()
    from_base = int(from_base)
    to_base = int(to_base)
    return convert_internal(number, from_base, to_base)
