#!/usr/bin/env python3
import sys
import re

params = sys.argv[1:]

if len(params) == 0:
   print("none")
else:
   for text in params:
        if not text.endswith("ism"):
            print(text + "ism")

