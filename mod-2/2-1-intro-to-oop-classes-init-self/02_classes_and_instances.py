# Classes and Instances: a class puts the data and the functions that work on it in the same place.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- Defining a Class ----------
class Event:
    pass


jazz = Event()
pottery = Event()

print(type(jazz))       # <class '__main__.Event'>
print(type(pottery))    # <class '__main__.Event'>
print(jazz is pottery)  # False: each call to Event() makes a separate object

# Attributes added one at a time, by hand
jazz.name = 'Friday Night Jazz'
jazz.date = date(2026, 12, 5)

pottery.name = 'Intro to Pottery'

# print(pottery.date)  # crashes on purpose: AttributeError: 'Event' object has no attribute 'date'


# # ---------- __init__ Gives Every Instance the Same Shape ----------
# # Python runs __init__ every time you create an instance, and passes the new instance in as self.

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#         self.seats_sold = 0
#
#
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
#
# print(jazz.name)          # Friday Night Jazz
# print(pottery.capacity)   # 2
#
# # # Leaving out an argument now fails on the line that made the mistake:
# # Event('Intro to Pottery', date(2026, 11, 20))  # crashes on purpose: TypeError, missing 'capacity'
#
# # # Predict, then run: both events are made from the same class. What prints?
# print(pottery.capacity)
# print(jazz.capacity)


# # ---------- Data Goes on self ----------
# # This version forgets self. on one line, so seats_sold disappears when __init__ finishes.

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#         seats_sold = 0
#
#
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# print(jazz.name)        # Friday Night Jazz
# # print(jazz.seats_sold)  # crashes on purpose: AttributeError: 'Event' object has no attribute 'seats_sold'
