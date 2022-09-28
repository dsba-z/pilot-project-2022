def input_int(prompt="", start=0, end=int):
    while True:
        try:
            input_string = input(prompt)
            number = int(input_string)
            if number >= start and end is not None and number <= end:
                return number
            print(f"Number should be between {start} and {end}.")
        except ValueError:
            print("Input should be an integer number")
