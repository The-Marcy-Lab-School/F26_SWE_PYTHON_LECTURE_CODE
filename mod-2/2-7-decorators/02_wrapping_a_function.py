# Wrapping a Function: announce() takes a function and returns a wrapper that runs code before and after it.
# Uncomment one section at a time as the lesson goes on.


def announce(func):                 # takes a function as its parameter
    def wrapper(name):              # the wrapper, defined inside announce()
        print('--- starting ---')   # runs before func
        func(name)                  # wrapper closes over func, so it can call func later
        print('--- finished ---')   # runs after func
    return wrapper                  # returns the wrapper without calling it


def greet(name):
    print(f'Hi, {name}!')


greet('Maya')
# Hi, Maya!

announced_greet = announce(greet)   # announced_greet now refers to wrapper
announced_greet('Maya')
# --- starting ---
# Hi, Maya!
# --- finished ---


# # ---------- Predict, then run ----------
# # In what order do these four lines print?

announced_greet = announce(greet)
# print('ready')
# announced_greet('Maya')


# # ---------- Challenge: Keep the Return Value ----------
# # announce() throws away whatever the wrapped function returns, so the last line prints None.
# # Fix wrapper in announce() at the top of this file so that the last line prints HI, MAYA! instead.

def shout(name):
    return f'HI, {name.upper()}!'


announced_shout = announce(shout)
# print(announced_shout('Maya'))
# # --- starting ---
# # --- finished ---
# # None


# # ---------- Decorators and the @ Syntax ----------

@announce          # the decorator: the same as greet = announce(greet) after the definition
def greet(name):
    print(f'Hi, {name}!')


# greet('Maya')      # greet now refers to the wrapper
# # --- starting ---
# # Hi, Maya!
# # --- finished ---


# # ---------- Predict, then run ----------
# # This version of announce() prints a line as soon as announce() is called, before building the wrapper.
# # func.__name__ is a function's name as a string. In what order do the lines print?

def announce(func):
    print(f'decorating {func.__name__}')
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


# @announce
# def greet(name):
#     print(f'Hi, {name}!')
#
#
# print('ready')
# greet('Maya')
