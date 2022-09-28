def input_int(prompt="", start=0, end=10):
    while True:
        try:
            input_string = input(prompt)
            number = int(input_string)
            if end is None:
                if start <= number:
                    return number
                print(f"Number should be greater than {start}.")
            else:
                if start <= number <= end:
                    return number
                print(f"Number should be between {start} and {end}.")

        except ValueError:
            print("Input should be an integer number")
