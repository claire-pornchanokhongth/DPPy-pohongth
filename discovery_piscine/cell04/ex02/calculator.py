#!/usr/bin/env python3
a = int(input("Give me the first number: "))
b = int(input("Give me the second number: "))
print("Thank you!")
for op, r in [
    ("+", a + b), 
    ("-", a - b), 
    ("/", a // b if a % b == 0 else a / b), 
    ("*", a * b)
    ]:
        print(f"{a} {op} {b} = {r}")