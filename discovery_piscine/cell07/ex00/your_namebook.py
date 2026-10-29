#!/usr/bin/env python3

def array_of_names(persons):
    names = []
    for first, last in persons.items():
        names.append(first.capitalize() + " " + last.capitalize())
    return names

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))