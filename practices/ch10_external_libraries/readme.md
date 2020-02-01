# Practice Exercises for external packages

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### requirements.txt

When working with an application that uses external packages, you need to communicate what packages are required for it to run. We do this with a `requiements.txt` file, here is an example:

```
colorama
prompt_toolkit
```

Once you have a virtual environment active, you can install all the dependencies with this command:

```
(env) C:\> pip install -r requirements.txt
```

###  Virtual environments

Virtual environments are key to having different versions of the same library coexisting on your computer. You create one as follows: 

#### macOS / Linux

```
$ python3 –m venv venv
$ . venv/bin/activate
```

#### Windows

```
C:\> python –m venv venv
C:\> venv\scripts\activate
```

### pip

Pip is the tool you use on the command line to install and view external packages. Here are some examples:

```bash
$ pip list
$ pip install colorama
$ pip install -r requirements.txt
$ pip uninstall requests
```

## Exercises

Now it's your turn. In this practice, go back to the tic tac toe game we created back in the chapter on problem solving. Alternatively, if you made it through Connect 4, you can work with that one instead. Your job will be to:

* Create a virtual environment.
* Set it as the active python interpreter in PyCharm under `settings > project > project interpreter`.
* Create a requirements.txt file with `colorama` as a dependency.
* Install the requirements with `pip`.
* Use `colorama` to add colored output to your game.