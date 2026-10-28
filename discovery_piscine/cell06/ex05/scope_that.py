#!/usr/bin/env python3

def add_one(number):
   number = number + 1

#def add_one(number):
 #  return number + 1

value = 42
print(value)
add_one(value)
print(value)

value = add_one(value)
print(value)
