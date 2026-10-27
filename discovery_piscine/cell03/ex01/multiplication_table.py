#!/usr/bin/env python3
print("Enter a number")
number = int(input().strip())
i = 0
while i <= 9:
    print(i, "x", number, "=", i * number)
    i = i + 1
