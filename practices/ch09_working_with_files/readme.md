# Practice Exercises for file I/O

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### Determining the full path to a file

Remember that the file location when loading files like `the_file.txt` depend on the working directory, which your program probably doesn't control. So we need to use the `os` module to work from known locations.

```python
directory = os.path.dirname(__file__)
filename = os.path.join(directory, 'the_file.txt')
# Now filename is a full path
```

###  Opening a file for reading

To open a file we use, well, the `open()` function. But as we saw, we should do this within a `with` block to ensure it's closed and flushed in a timely manner. Note the **r** passed to open for read.

```python
with open(filename, 'r', encoding='utf-8') as fin:
    # work with fin here
    
# fin is closed and useless at this point.
```

### Writing to a file

Writing to a file is similar to reading, it's just about how you open it. Note the **w** for write and **fout** to tell us that it's an output not input file stream.

```python
with open(filename, 'w', encoding='utf-8') as fout:
    # work with four here
```

### Using json module with file streams

Given a file stream, json can read or write objects to/from the json file format.

```python
import json

# load the rolls from fin input stream
rolls = json.load(fin)

# save the leader dictionary to the fout file stream
json.dump(leaders, fout)
```

## Exercises

Now it's your turn. In this practice, go back to the tic tac toe game we created back in the chapter on problem solving. Alternatively, if you made it through Connect 4, you can work with that one instead. Your job will be to:

* Add a leader board (feel free to use JSON like we did).
* Add a running log file (test with `tail -n 20 -f FILENAME` on macOS and Linux, just open in PyCharm on Windows and it'll change).
* For extra credit, you can try to use [LogBook](https://logbook.readthedocs.io/en/stable/) to improve the logging (but it will require a few concepts we haven't covered yet).