# Advanced Topics
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- Comparing with an Object of Another Type ----------
# This __eq__ assumes other has a name and a date.
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# print(jazz == 'Friday Night Jazz')  # crashes on purpose: AttributeError: 'str' object has no attribute 'name'


# # ---------- Checking the Type First ----------
# # NotImplemented tells Python this method cannot compare the two, so Python falls back to identity.

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#
#     def __eq__(self, other):
#         if not isinstance(other, Event):
#             return NotImplemented
#         return self.name == other.name and self.date == other.date
#
#
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# print(jazz == 'Friday Night Jazz')  # False


# # ---------- Objects with __eq__ Cannot Be Dictionary Keys ----------
# # Defining __eq__ removes the hash a dictionary needs from its keys.

# # tickets_sold = {jazz: 3}  # crashes on purpose: TypeError: cannot use 'Event' as a dict key (unhashable type: 'Event')
#
# # # Key the lookup table by something hashable that identifies the event, such as its name:
# tickets_sold = {jazz.name: 3}
# print(tickets_sold['Friday Night Jazz'])  # 3
