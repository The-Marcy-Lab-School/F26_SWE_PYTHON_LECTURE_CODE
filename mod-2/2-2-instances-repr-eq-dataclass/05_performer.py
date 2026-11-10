# ---------- Challenges: A Readable Performer, Equal Performers, and Refactor Performer with @dataclass 🏗️🏗️🏗️🏗️🏗️ ----------
# The venue books performers for its concerts. Build Performer in three steps:
# 1. A Readable Performer: store the name and the genre in __init__, and add a __repr__
#    so that printing a performer shows Performer('The Blue Notes', genre='jazz').
# 2. Equal Performers: add an __eq__ so that two performers are equal when they have the same name and genre.
# 3. Refactor Performer with @dataclass: rewrite the class with @dataclass, so that it defines no methods by hand,
#    and compare what the print() calls show before and after.
# Run the file after each step. It runs before you start, and shows memory addresses and False until each step is done:
#     python3 05_performer.py

from dataclasses import dataclass


class Performer:
    def __init__(self, name, genre):
        pass  # store both on self

    # Step 1: add __repr__ here

    # Step 2: add __eq__ here


blue_notes = Performer('The Blue Notes', 'jazz')
print(blue_notes)                                       # should print Performer('The Blue Notes', genre='jazz')
print([blue_notes, Performer('Lena Ortiz', 'folk')])    # should print [Performer('The Blue Notes', genre='jazz'), Performer('Lena Ortiz', genre='folk')]

print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'jazz'))   # should print True
print(Performer('The Blue Notes', 'jazz') == Performer('The Blue Notes', 'blues'))  # should print False
