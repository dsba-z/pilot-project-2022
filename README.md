# Pilot project

## Introduction

This project serves as a compilation of solutions of some workshop tasks and as an example for practice with larger projects.

The intention is for students to provide pull requests to this repository with new features and additions. Each addition will give bonus points.

Several people **can** submit a pull request for the same feature, especially when they didn't discuss it beforehand. Only one of them will most likely be merged, but both can give points.

## Planned features

1. Interactive console interface.
2. Using command line arguments with `argparse`.
3. Web interface

The main idea is to make a large directory of options and then select them. There shouldn't be any complex interactions, just some interface like:

```
Choose option:
0. Exit.
1. Convert an integer from any base to any base.
2. Figure out if a knight can get from square A to square B.
3. Calculate the mean for a sequence of data.
4. Solve problem X from Contest #Y.
...
```

Each option here leads to a single function which takes a line of data and provides some output.

## Code style

For this repository there is a requirement of relatively good code style. Use *pylint*, *flake8* or PyCharm "Problems" tab to check for style errors. Zero errors means good enough.

Please use double quotation marks for strings: `"a string"`.

## Init

Project requires a few external libraries. You can install them using `pip` in your Terminal.

Just open the terminal in project's directory and run
```
pip install -r requirements.txt
```

## TODO

These are potential features you may implement to get bonus points.

### Better console interface (~2-5 points)

Right now for simplicity the interface only works with a single line of input. The inputs are not documented at all. A better version would work like this:

```
Choose option:
0. Exit.
1. Convert number from any base to any base.
2. Solve the knight move problem.
...
> 1
Enter the original base:
> 2
Enter the target base
> 10
Enter the number in the original base:
> 1111
Answer:
15 
```

You don't have to modify all the tasks to use this feature. The main problem here is to implement it for one task, so that it can be reused for others late.

Points vary by how general and how well integrated your solution is.

### argparse (~2-7 points)

Add an ability to call the program like this instead of working interactively:

```
python main.py --problem 1 --input 2 10 1111
> Solving problem "Convert number from any base to any base"
> Input is 2 10 1111
> Answer is 15
```

Calling it without any command line arguments should still enable the interactive mode.

Points vary by how general and how well integrated your solution is.


### General clean-up and refactoring (~1-5 points)

Add things that make the program work smoother.

- Checking input correctness.
- Retrying on failed input.
- Better output formatting (maybe try `pprint`).
- Other features you think are worth it.

### Flask web interface (low priority) (~2-10 points)

I plan to implement it myself, but you may try to make your own implementation if you want to really get ahead.

Web interface will work through Flask. The main page should contain a list of tasks as links. Each link goes to a page with text input forms and a button that runs the task.

