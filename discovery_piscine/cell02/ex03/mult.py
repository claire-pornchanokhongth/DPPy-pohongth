#!/usr/bin/env python3
first_number = int(input("Enter the first number: ").strip())
second_number = int(input("Enter the second number: ").strip())
result = first_number * second_number
print(first_number, "x", second_number, "=", result)
if result < 0:
    print("The result is negative.")
elif result > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
