# Practice exercises for interactive code

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### Running Python code

If you have a Python **file**, it can be executed inside PyCharm by simply right-clicking and choosing **Run**. Outside of PyCharm, you execute it like this:

```bash
$ python3 program.py

# or 

C:\> python program.py 
```

Remember to use either `python` or `python3` based on your system setup. 

### if / else statements

The essential lesson from this chapter is how code makes decisions to do one thing or another. The first building block are simple **this or that** type of processes. These are done with `if` statements.

```python
num = 7

if num < 100:
    print("Number is smallish")
```

We can also have code that has two or more branches with `elif` and `else`:

```python
num = 7

if num < 100:
    print("Number is smallish")
elif num < 1000:
    print("Middle sized number.")
else:
    print("That's one big number!")
```

### while loops

When you need to repeat an operation as long as some condition is met, the `while` loop is the thing you want.

```python
attempts = 0

while attempts < 5:
    attempts += 1
    # do whatever you are attempting here...
```

### Is a number even or odd?

This seems like a simple question to answer but requires a new operation. The modulo operator. This is basically the remainder of a division. For example, 19 / 5 is 3 as a **whole number** (int). But we know that there is a remainder of 4 for whole number math. In Python we express this as:

```python
div = int(19 / 5)  # <-- 3
rem = 19 % 5       # <-- 4
```

Then we can test whether a number is even if it is evenly divisible by 2 or has a remainder of 0:

```python
remainder = num % 2  # Is this 0 or 1?
```


## Exercises

Now it's your turn. Here are some ideas to practice. 

1. Create a **hello_world.py** file and execute it with Python. This can be in PyCharm or in another editor and using the technique above. Seems trivial but will help you verify everything is working right there. Just have the program output "Hello world"
2. Write a program that requests a number from the user. Have the program print "Even" or "Odd" depending on whether they entered an even or odd number.
3. Extend the program above to repeatedly ask that question as long as the user enters a nonzero number. But if they enter 0, it should then stop asking and say goodbye.
4. Take one of these sets of code and visualize them with [pythontutor.com](http://pythontutor.com/visualize.html#mode=edit)
