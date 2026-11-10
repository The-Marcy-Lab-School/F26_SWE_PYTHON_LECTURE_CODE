# What is a data type? And what is a class?
# Uncomment one section at a time as the lesson goes on.

from datetime import date

# type() returns the type of data it is given.
print(type('hello'))        # <class 'str'>
print(type(3.5))            # <class 'float'>
print(type(['A1', 'A2']))   # <class 'list'>


# # ---------- Every Value is an "Instance" of a "Class" ----------
# # Calling a class creates an instance of it. Quotes are a shortcut for making a string.

# favorite_number = '42'
# boiling_point = str(212)
#
# print(type(favorite_number))    # <class 'str'>
# print(type(boiling_point))      # <class 'str'>
#
# # # Most other classes, such as date, can only be instantiated by calling the class:
# knicks_victory = date(2026, 6, 13)
# print(type(knicks_victory))     # <class 'datetime.date'>
#
# marcy_founded = date(2019, 9, 20)
# print(type(marcy_founded))      # <class 'datetime.date'>


# # ---------- dir Tells Us what a Class and its Instances Can Do ----------
# # float() turns a string into a new float instance. '3.5' stands in for what input() returns.

# user_input = '3.5'
# print(type(user_input))  # <class 'str'>
#
# user_float = float(user_input)
# print(type(user_float))  # <class 'float'>
#
# # # dir() lists every name a value answers to. The dunder methods come first.
# print(dir('hello'))
# print(dir(5.5))
#
# print('upper' in dir('hello'))  # True
# print('upper' in dir(5.5))      # False
#
# print('hello'.upper())  # HELLO
# # print(5.5.upper())  # crashes on purpose: AttributeError: 'float' object has no attribute 'upper'
#
# # # - calls __sub__, which float defines and str does not:
# print(5.5 - 2.0)  # 3.5
# # print('hello' - 'world')  # crashes on purpose: TypeError: unsupported operand type(s) for -: 'str' and 'str'


# # ---------- Instances Find Their Methods in Their Class ----------
# # Every string finds its methods in the str class, so the two lists match.

# print(dir(str) == dir('hello'))  # True
#
# print(str.upper('hello'))   # HELLO
# print('hello'.upper())      # HELLO
#
# # # Predict, then run: is __add__ one of the names in dir(list)? Will the + work, or raise an error?
# print(dir(list))
# print([1, 2, 3] + [4, 5, 6])
