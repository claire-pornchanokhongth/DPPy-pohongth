#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("none")
else:
    table = 0
    while table <= 10:
        line = "Table de " + str(table) + ":"
        i = 0
        while i <= 10:
            line = line + " " + str(table * i)
            i = i + 1
        print(line)
        table = table + 1
