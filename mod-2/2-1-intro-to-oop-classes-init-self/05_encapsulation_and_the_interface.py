# Encapsulation and the Interface: keeping related data together, along with the rules about it.
# Uncomment one section at a time as the lesson goes on.

from datetime import date

# ---------- Parallel Lists Drift Apart ----------
names = ['Movie Night: Coco', 'Friday Night Jazz', 'Intro to Pottery']
capacities = [30, 40, 2]
seats_sold = [5, 12, 2]


def seats_left(i):
    return capacities[i] - seats_sold[i]


print(f'{names[1]}: {seats_left(1)} seats left')
# Friday Night Jazz: 28 seats left

names.sort()  # sorts the names but not the capacities or seats_sold

print(f'{names[1]}: {seats_left(1)} seats left')
# Intro to Pottery: 28 seats left -- but the workshop is sold out


# # ---------- Dictionaries Keep the Data Together but Not the Rules ----------
# # Each event's data lives in one record, but the rule lives in separate functions.

# def make_event(name, capacity):
#     return {'name': name, 'capacity': capacity, 'seats_sold': 0}
#
#
# def seats_left(event):
#     return event['capacity'] - event['seats_sold']
#
#
# def sell_ticket(event):
#     if seats_left(event) == 0:
#         print(f"{event['name']} is sold out.")
#         return
#     event['seats_sold'] += 1
#
#
# pottery = make_event('Intro to Pottery', 2)
# sell_ticket(pottery)
# sell_ticket(pottery)
# sell_ticket(pottery)    # Intro to Pottery is sold out.
#
# # # Nothing connects the dictionary to sell_ticket(), so any line can change the record directly:
# pottery['seats_sold'] += 1
# print(seats_left(pottery))    # -1


# # ---------- One Place for the Data and Its Rules ----------

# class Event:
#     def __init__(self, name, date, capacity):
#         self.name = name
#         self.date = date
#         self.capacity = capacity
#         self.seats_sold = 0
#
#     def seats_left(self):
#         return self.capacity - self.seats_sold
#
#     def sell_ticket(self):
#         if self.seats_left() == 0:
#             print(f'{self.name} is sold out.')
#             return
#         self.seats_sold += 1
#
#     def can_refund(self, today):
#         return today < self.date
#
#
# # The class version: the rule is a method of the event
# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
# pottery.sell_ticket()
#
# # Read past the dunder methods at the start of the list to find what this class gave the event
# print(dir(pottery))
#
# # So far the constraint is an agreement rather than a lock: this line still goes around the rule
# pottery.seats_sold = 99
# print(pottery.seats_left())  # -97


# # ---------- The Interface ----------
# # The interface for changing an event's seats is sell_ticket(), where the sold-out check runs.

# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
# pottery.sell_ticket()
# pottery.sell_ticket()
# pottery.sell_ticket()        # Intro to Pottery is sold out.
# print(pottery.seats_sold)    # 2: reading seats_sold is fine
# print(pottery.seats_left())  # 0


# # ---------- Dictionary or Class? ----------
# # Data with no rules or actions of its own, such as a lookup table, suits a dictionary.

# room_rates = {'Dance Studio': 40, 'Main Hall': 150}
# print(room_rates['Main Hall'])  # 150
