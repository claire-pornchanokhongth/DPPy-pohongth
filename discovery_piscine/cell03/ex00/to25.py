#!/usr/bin/env python3
print("Enter a number less than 25")
number = int(input().strip())
if number > 25:
    print("Error")
else:
    while number <= 25:
        print("Inside the loop, my variable is", number)
        number = number + 1
