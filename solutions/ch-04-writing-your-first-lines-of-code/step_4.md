## Step 4: Use the built-in library datetime
 
Use the built-in library datetime and the function `datetime.datetime.now()` 
to determine the current year and print that to REPL using an f-string. 


```
>>> import datetime
>>> right_now = datetime.datetime.now()
>>> # What is this thing?
>>> right_now
datetime.datetime(2020, 7, 10, 14, 41, 33, 790353)
>>> print(f"What a crazy year {right_now.year} has been, eh?")
What a crazy year 2020 has been, eh?
>>> 
```
