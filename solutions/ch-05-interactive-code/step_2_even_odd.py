print("Let's talk about numbers!")
print()

num_text = input("What's your favorite whole number? ")
num = int(num_text)

if num % 2 == 0:
    print(f"What a sweet number, {num:,} is even!")
else:
    print(f"That's odd. Yeah, I mean {num:,} is an odd number mathematically.")

# Note:
# {num:,} does digit grouping: 10101010 -> 10,101,010
# {num} would just repeat it as 10101010.
