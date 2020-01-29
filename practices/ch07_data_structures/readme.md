# Practice exercises for data structures

## Overview

In this section, you'll have a chance to practice the concepts you've learned in the videos. First, review the core concepts covered that you'll need to keep in mind. Then go through the exercises below. 

Remember, these are for your own benefit. Feel free to skip them if you don't find a particular exercise valuable or you get stuck for too long.

## Core concepts

### Creating a static dictionary

You can create a dictionary a number of ways. How you do this depends on how much data is static and how much is dynamic as part of the program's execution.

```python
# Static data styles:

# empty dictionary
names = {}

# A dictionary with players start at zero score
two_names = {'player1': 0, 'player2': 0} 

# This is the same as before
two_names = dict(player1=0, player2=0) 
```

### Creating a dynamic dictionary

If you have dynamic data, this requires something else to build them:

```python
names = get_list_of_names()
scores = {}
for n in names:
     scores[n] = 0
     
# We can condense this using a dictionary comprehension. 
# Same as above:
names = get_list_of_names()
scores = {n: 0 for n in names} 
```

### Reading values from a dictionary

```python
# Access a *known* value in the dictionary:
p1_score = scores['player1']

# Access a score, unsure whether player1 is a key, if it isn't there, return 0.
p1_score = scores.get('player1', 0)
```

## Exercises

Now it's your turn. Try this practice below.

The core idea in this chapter was about dictionaries and data structures in general. Create a simple program that creates a dictionary called `d` such that the following runs without error and prints what is expected:

```python
# d = create d using core concepts above.

print(d["Sam"])          # outputs 7
print(d['rolls'])        # outputs ['rock', 'paper', 'scissors']
print(d.get('Sarah'))    # outputs None
print(d.get('Jeff', -1)) # outputs -1
print(d['done'])         # outputs True
```
