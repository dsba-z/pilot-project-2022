# Pilot project

## Introduction

This project serves as a compilation of solutions of some workshop tasks and as an example for practice with larger projects.

The intention is for students to provide pull requests to this repository with new features and additions. Each addition will give bonus points.

## Planned features

1. Interactive console interface.
2. Using command line arguments with `argparse`.
3. Web interface

The main idea is to make a large directory of options and then select them. There shouldn't be any complex interactions, just some interface like:

```
Choose option:
1. Convert an integer from any base to any base.
2. Figure out if a knight can get from square A to square B.
3. Calculate the mean for a sequence of data.
4. Solve problem X from Contest #Y.
...
0. Exit.
```

Each option here leads to a single function which takes a line of data and provides some output.

## Code style

For this repository there is a requirement of code style. Use *pylint*, *flake8* or PyCharm "Problems" tab to check for style errors. 

## Init

Project requires a few external libraries. You can install them using `pip` in your Terminal.

Just open the terminal in project's directory and run
```
pip install -r requirements.txt
```