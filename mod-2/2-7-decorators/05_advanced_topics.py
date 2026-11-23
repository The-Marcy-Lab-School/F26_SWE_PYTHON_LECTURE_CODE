# Advanced Topics: wrapping a function that takes any arguments, and keeping a method's name with functools.wraps.
# Uncomment one section at a time as the lesson goes on.


# A wrapper written as def wrapper(name): can only wrap functions that take exactly one argument.
def announce(func):
    def wrapper(name):
        print('--- starting ---')
        func(name)
        print('--- finished ---')
    return wrapper


@announce
def seat_label(row, number):
    return f'{row}{number}'


# seat_label('B', 12)   # crashes on purpose
# TypeError: announce.<locals>.wrapper() takes 1 positional argument but 2 were given


# # ---------- Wrapping a Function That Takes Any Arguments ----------

def announce(func):
    def wrapper(*args, **kwargs):           # collects any positional and keyword arguments
        print('--- starting ---')
        result = func(*args, **kwargs)      # passes them all on to func unchanged
        print('--- finished ---')
        return result
    return wrapper


@announce
def seat_label(row, number):
    return f'{row}{number}'


# print(seat_label('B', 12))                 # B12, after the two announcements
# print(seat_label(row='C', number=3))       # C3, after the two announcements


# # ---------- Keeping a Method's Name with functools.wraps: the problem ----------

def requires_paid(method):
    def wrapper(self):
        if self.status != 'paid':
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return
        return method(self)
    return wrapper


class Reservation:
    @requires_paid
    def check_in(self):
        self._status = 'checked_in'


# print(Reservation.check_in.__name__)   # wrapper


# # ---------- Keeping a Method's Name with functools.wraps: the fix ----------

from functools import wraps


def requires_paid(method):
    @wraps(method)                          # copies method's name onto wrapper
    def wrapper(self):
        if self.status != 'paid':
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return
        return method(self)
    return wrapper


class Reservation:
    @requires_paid
    def check_in(self):
        self._status = 'checked_in'


# print(Reservation.check_in.__name__)   # check_in
