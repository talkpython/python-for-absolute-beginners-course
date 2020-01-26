# Practice exercises for organizing with functions

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### Function with parameters (input data)

When we have code that we want to reuse or isolate and treat as a single concept (black box), we define functions. Here is a basic function:

```python
def say_hello(name):
    print(f'Nice to meet you {name}') 
```

### Function that generates data (return values)

Functions can also return values to be used later:

```python
def get_name():
   name = input("What is your name? ") 
   return name 
```

We can then use these functions together as follows:

```python
person = get_name()
say_hello(person)
```

### A main method and running "the program"

As we saw, it's a good convention to have an overall organizing function that is what the whole program does at the top of the file. I called this main, for example:

```python
def main():
    show_header()
    get_names()
    # ... 
```

And you must remember to run this **at the end** of your program to actually make it execute. We added these two lines as the final of the source file:

```python
if __name__ == "__main__":
    main()
```

## Exercises

Now it's your turn. Your practice exercise is to **take the M&M guessing game we created back in chapter 5 (interactive code) and clean it up using functions**. Make a copy of the file in this folder called `guessinggame.py`. That's what we started with. There are probably 3-4 functions that you can create to help organize and isolate parts of this application. Use the core concepts above to help. 