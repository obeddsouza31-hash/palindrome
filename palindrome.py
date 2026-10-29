import sys

def is_palindrome(n):
    return str(n) == str(n)[::-1]

if len(sys.argv) > 1:
    numbers = sys.argv[1:]
else:
    numbers = ["121"]

for value in numbers:
    if not value.isdigit():
        print("Please enter a valid positive integer")
        sys.exit(1)

    n = int(value)

    if is_palindrome(n):
        print(n, "is a palindrome")
    else:
        print(n, "is not a palindrome")
