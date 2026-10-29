#!/usr/bin/env python3
import sys

def shrink(text):
    print(text[:8])

# shrink("123456789")

def enlarge(text):
    while len(text) < 8:
        text += "Z"
    print(text)

# enlarge("123")

params = sys.argv[1:]

if len(params) < 1:
    print("none")
else:
    for arg in params:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)