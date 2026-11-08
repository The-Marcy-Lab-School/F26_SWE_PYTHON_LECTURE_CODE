# How does upper() know which string to capitalize? Its parentheses are empty.
# Uncomment one section at a time as the lesson goes on.

from datetime import date

print('hello'.upper())  # HELLO

seats = ['A1', 'A2']
seats.append('A3')
print(seats)  # ['A1', 'A2', 'A3']


# # ---------- Idea 1. Every Value Comes from a Class ----------
# # type() returns the class a value was made from.

# print(type('hello'))              # <class 'str'>
# print(type(['A1', 'A2']))         # <class 'list'>
# print(type(3.5))                  # <class 'float'>
# print(type(date(2026, 12, 5)))    # <class 'datetime.date'>
#
# # float() turns a string into a new float instance. '3.5' stands in for what input() returns.
# user_input = '3.5'
# print(type(user_input))  # <class 'str'>
#
# user_float = float(user_input)
# print(type(user_float))  # <class 'float'>


# # ---------- Idea 2. The Methods Available to a Value Live in its Class ----------
# # dir() lists every name a value answers to. The dunder methods come first, then the methods you already use.

# print(dir('hello'))
# print(dir(str))  # the same list: the methods live in the class
#
# print('upper' in dir('hello'))  # True
# print('hello'.upper())          # HELLO
#
# print('upper' in dir(5.5))      # False
# # print(5.5.upper())  # crashes on purpose: AttributeError: 'float' object has no attribute 'upper'


# # ---------- Idea 3. The Value Before the Dot Is the First Argument ----------
# # Python finds the method in the value's class and calls it with the value as the first argument.

# print(str.upper('hello'))    # called on the class str, with 'hello' as the argument -> HELLO
# print('hello'.upper())       # called on the string instance with no argument -> HELLO
#
# # # Predict, then run: each call is written on the class instead of on the value. What prints?
# seats = ['A1', 'A2']
# list.append(seats, 'A3')
# print(seats)
#
# print(str.upper('sold out'))


# # ---------- Challenge: Rewrite the Call ----------
# # For each value, use type() to name its class, check with dir() that the method is there,
# # then rewrite the call so that it is made through the class. Each rewrite should print the same result.
#
# # # For example:
# email = 'MAYA@EXAMPLE.COM'
# print(email.lower())            # maya@example.com
# print(type(email))              # <class 'str'>
# print('lower' in dir(email))    # True
# print(str.lower(email))         # maya@example.com
#
# # # Your turn:
# event_names = ['Friday Night Jazz', 'Intro to Pottery', 'Friday Night Jazz']
# print(event_names.count('Friday Night Jazz'))  # 2
#
# price = 25.0
# print(price.is_integer())  # True
