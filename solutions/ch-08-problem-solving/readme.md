## Solution for Connect4

This one is VERY similar to TIC-TAC-TOE. There are three fundamental changes, other
than this, it's the same code for both games.

### Change 1: Board data structure.

We are using this data structure. Tic-Tac-Toe was 3x3. Connect4 is 7x6 (7 columns, 6 rows):

```python
# Board is a list of rows
# Rows are a list of cells
board = [
    # 6 rows
    [None, None, None, None, None, None, None],  # 7 columns per row
    [None, None, None, None, None, None, None],  # 7 columns per row
    [None, None, None, None, None, None, None],  # 7 columns per row
    [None, None, None, None, None, None, None],  # 7 columns per row
    [None, None, None, None, None, None, None],  # 7 columns per row
    [None, None, None, None, None, None, None],  # 7 columns per row
]
```

### Change 2: You pick a column, drop the disk, it falls down

The second major change is how you pick where to play.

In Tic-Tac-Toe, it's choose the square. In Connect 4, it's choose the column,
drop the disk it fall as far as it can. We rewrote `choose_location()` accordingly.

### Change 3: Finding lists of 4 in the rows, cols, and diagonals

The final major change is finding wins. In Tic-Tac-Toe, we wrote a function called:

```python
def get_winning_sequences(board):
    ...
```

This function would turn rows, columns, and diagonals into just straight lists. Then
they are super simple to check. Are all of them one of the same kind and not empty?
For example, is a diagonal all X's? Then X's win.

It's identical in connect 4. But finding these are a bit of a pain. You don't have to have 
the whole row, or column, or diagonal the same to win. You just need 4 in a row of these.

So we wrote a function called `find_sequences_of_four_cells_in_a_row(cells)`. It
takes a series of items, say 7 items, then returns all consecutive possibilities of 4.

For example:

```python
cells = [1, 2, 3, 4, 5, 6]
fours = find_sequences_of_four_cells_in_a_row(cells)
# fours = [
#    [1, 2, 3, 4], 
#    [2, 3, 4, 5], 
#    [3, 4, 5, 6]
#]
```

Then we can just return these out of `get_winning_sequences()` and it'll see if any are winners. 
At that point, it's all the same as Tic-Tac-Toe. If they are all one type, that type is the winner.

Finding the sequences is a bit more complex, but it's the same idea. Find all possible diagonals,
rows, and columns, use `find_sequences_of_four_cells_in_a_row()` to find the lists of 4 and check them.

That's the game.

See [connect4.py](./connect4.py)
