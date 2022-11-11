import os


def task1(d):
    output = ''

    def print_dir(cum, level=0):
        nonlocal output
        for file in os.scandir(cum):
            if os.path.isfile(file):
                output += '\t' * level + '|-' + file.name + '\n'
            elif os.path.isdir(file):
                output += '\t' * level + '|-' + file.name + '/' + '\n'
                print_dir(cum + '/' + file.name, level + 1)

    try:
        print_dir(d)
    except:
        return ''

    print(output)
    return output
