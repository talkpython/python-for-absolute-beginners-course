print("Let's talk about numbers!")
print()

question_text = "Give me a whole number [0 to cancel]? "

num_text = input(question_text)
num = int(num_text)

while num != 0:

    if num % 2 == 0:
        print(f"What a sweet number, {num:,} is even!")
    else:
        print(f"That's odd. Yeah, I mean {num:,} is an odd number mathematically.")

    # Note:
    # {num:,} does digit grouping: 10101010 -> 10,101,010
    # {num} would just repeat it as 10101010.

    num_text = input(question_text)
    num = int(num_text)

print("kthxbye!")
