# Practice Exercises for first lines of code

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### REPL

REPL stands for Read-Eval-Print-Loop and is the interactive environment you get when you type `python` in the terminal / command prompt. Remember, on macOS and Linux, you start Python 3's REPL by typing `python3`.

### Variables and values

Variables are names that we use to refer to data that could change or is complex to write directly. Values are the data that is currently assigned to that variable. We used [pythontutor.com](http://pythontutor.com) to explore this.

Examples:

```python
x = 7
y = 11
z = x + 2*y 
name = 'Sarah'
```

### Using built-in libraries

Python comes with many included libraries ([hundreds!](https://docs.python.org/3/library/)). To use one of these libraries, such as `sys`, you must tell Python you want to load it. This is done with the `import` keyword. 

Example:

```python
import sys
print(f"The current version of Python is {sys.version_info}")
```

### Getting input from users

Getting input from users is done with the `input` function.

Example:

```python
name = input("What is your name? ")
print(f"Hello {name}")
```

#### Converting data

Certain operations (like math and string concatenation) require the correct data types.

Data is converted to numerical types using the type name (int, float, etc). Here are a few examples:

```python
text = '7.2'
whole_number = int(text)   # value = 7
number       = float(text) # value = 7.2
```

## Exercises

Now it's your turn. Here are some ideas to practice. 

1. Run the Python REPL and verify you have Python 3.6 or higher.
2. Create a variable which is a whole number, compute the square and cube of it (i.e. x^2 and x^3, although that is not the Python code needed).
3. Ask a user for their name and age. Write code to tell them how many years you are older than them (negative numbers for younger is fine at this point).
4. Use the built-in library `datetime` and the function `datetime.datetime.now()` to determine the current year and print that to REPL using an f-string.
5. Take one of these sets of code and visualize them with [pythontutor.com](http://pythontutor.com/visualize.html#mode=edit)
