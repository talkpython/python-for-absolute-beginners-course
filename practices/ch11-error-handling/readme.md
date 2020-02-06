# Practice Exercises for error handling

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### try / except

When handling errors, we can check for bad values (e.g. `None` where a proper string was expected). But Python's native error handling approach is exception-based: throwing and catching exceptions.

Below is the minimum code to catch an error in Python.

```python
try:
    do_risky_thing1()
    do_risky_thing2()
    do_risky_thing3()
except Exception as x:
    # Deal with error, use x for help on what happened.
```

###  Multiple error types

The example above is good to catch errors. But it catches them all (well, almost all of them), and it treats them all the same. 

Below is code needed to handle different errors as well as unforeseen errors.

```python
try:
    do_risky_thing1()
    do_risky_thing2()
    do_risky_thing3()
except json.decoder.JSONDecodeError:
    # Handle malformed JSON error
except FileNotFoundError as fe:
    # Handle missing file error
except ValueError:
    # Handle conversion error.
except Exception as x:
    # Deal with error, use x for help on what happened.
```

**Note**: It is important that the most specific errors are listed first and the most general the last (`Exception`). Python selects the first (not best) match.

## Exercises

Now it's your turn. In this practice, go back to the tic tac toe game we created back in the chapter on problem solving. Alternatively, if you made it through Connect 4, you can work with that one instead. Your job will be to:

* Add error handling around the input processing in your program using try / except. Be as specific on the errors as possible. If you can determine the cause or type of error, give a specific message.
* Think of all other ways your app could crash or run into trouble. Get it to crash, check the error type in the traceback, and add the appropriate error handling for this as well.