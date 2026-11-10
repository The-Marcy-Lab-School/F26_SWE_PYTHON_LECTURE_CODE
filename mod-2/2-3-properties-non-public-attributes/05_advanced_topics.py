# Advanced Topics
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- A Getter That Reads Its Own Name ----------
# Reading self.capacity inside the capacity getter runs the getter again, and again.
class Event:
    def __init__(self, capacity):
        self._capacity = capacity

    @property
    def capacity(self):
        return self.capacity


pottery = Event(2)
# print(pottery.capacity)  # crashes on purpose: RecursionError: maximum recursion depth exceeded


# # ---------- Two Underscores ----------
# # Python stores self.__capacity under the name _Event__capacity, which still reaches the value.

# class Event:
#     def __init__(self, capacity):
#         self.__capacity = capacity
#
#
# pottery = Event(5)
# print(pottery._Event__capacity)   # 5
# # print(pottery.__capacity)  # crashes on purpose: AttributeError: 'Event' object has no attribute '__capacity'


# # ---------- Class Methods ----------
# # date.today() is called on the date class, and Python passes the class in as cls.

# today = date.today()
# print(today)        # the current date, such as 2026-11-16


# # ---------- Static Methods ----------
# # A static method receives neither self nor cls, so it is a plain function placed inside a class.

# class Venue:
#     @staticmethod
#     def is_valid_email(email):
#         if '@' not in email:
#             return False
#         domain = email.split('@')[-1]
#         return '.' in domain
#
#
# print(Venue.is_valid_email('maya@example.com'))   # True
# print(Venue.is_valid_email('sam'))                # False
