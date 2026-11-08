# Encapsulation and the Interface: the class bundles the data with its rules, and constrains how other code changes the data.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- One Place for the Data and Its Rules ----------
class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.seats_sold = 0

    def seats_left(self):
        return self.capacity - self.seats_sold

    def sell_ticket(self):
        if self.seats_left() == 0:
            print(f'{self.name} is sold out.')
            return
        self.seats_sold += 1

    def can_refund(self, today):
        return today < self.date


# The class version: the rule is a method of the event
pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
pottery.sell_ticket()

# Read past the dunder methods at the start of the list to find what this class gave the event
print(dir(pottery))

# So far the constraint is an agreement rather than a lock: this line still goes around the rule
pottery.seats_sold = 99
print(pottery.seats_left())  # -97


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
