## Solution for error handling in tic-tac-toe

The only part of this first pass on the game that could fail is choosing the location.

Did you notice that when it asks for a number, if you don't enter anything it crashes hard?

How about if you state too much? It asks for row and you answer 2,3 (row and column)? Boom again.

That's what we fixed here with `try/except`:

```python
def choose_location(board, symbol):
    try:
        row = int(input("Choose which row: "))

        row -= 1
        if row < 0 or row >= len(board):
            return False

        column = int(input("Choose which column: "))
        column -= 1
        if column < 0 or column >= len(board[0]):
            return False

        cell = board[row][column]
        if cell is not None:
            return False

        board[row][column] = symbol
        return True
    except ValueError as ve:
        print(f"Error: Cannot convert input to a number.")
        return False
    except Exception:
        # Not sure what else happened here, but didn't work.
        return False
```

For a more advanced version, you could edit the tic-tac-toe from files and make sure we have
permissions to save to the files and that they are in a correct format for `json` to read and so on.

See [tictactoe_errors_handled.py](./tictactoe_errors_handled.py)
