# Class Attributes and Attribute Lookup: one value every concert shares, and the order Python searches for a name.
# Uncomment one section at a time as the lesson goes on.

from datetime import date, timedelta


# ---------- Class Attributes ----------
# SERVICE_FEE is assigned in the class body, so there is one copy of it, and it belongs to Concert.
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def can_refund(self, today):
        return today < self.date

    def __repr__(self):
        return f'{type(self).__name__}({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Concert(Event):
    SERVICE_FEE = 5

    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer

    def ticket_price(self):
        return super().ticket_price() + Concert.SERVICE_FEE

    def can_refund(self, today):
        return today <= self.date - timedelta(days=7)


class Screening(Event):
    def can_refund(self, today):
        return False


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
print(jazz.ticket_price())   # 30


# # ---------- Predict, then run ----------
# # The venue raises the service fee for every concert, including the two already scheduled.
# # What do the two print() lines show?

# choir = Concert('Winter Choir', date(2026, 12, 19), capacity=80, base_price=10, performer='Riverside Singers')
#
# Concert.SERVICE_FEE = 6
#
# print(jazz.ticket_price())
# print(choir.ticket_price())
#
# Concert.SERVICE_FEE = 5   # set the fee back, so the rest of the file uses $5


# # ---------- Attribute Lookup ----------
# # Python searches the instance, then its class, then the superclass, then object, and stops at the first match.

# print(jazz.__dict__)
# # {'name': 'Friday Night Jazz', 'date': datetime.date(2026, 12, 5), 'capacity': 40, 'base_price': 25, 'performer': 'The Blue Notes'}
#
# print('SERVICE_FEE' in jazz.__dict__)       # False
# print('SERVICE_FEE' in Concert.__dict__)    # True: found one step up, on the class
# print('ticket_price' in Concert.__dict__)   # True: found on Concert, so Event's version is never reached
# print('__repr__' in Concert.__dict__)       # False
# print('__repr__' in Event.__dict__)         # True: found one step further up
# print('__ne__' in Event.__dict__)           # False
# print('__ne__' in object.__dict__)          # True: found at the last step
#
# # jazz.blah  # crashes on purpose: AttributeError: 'Concert' object has no attribute 'blah'


# # ---------- Q: A list [] holds its items, but where does a list's append() method live? ----------

# seats = ['A1', 'A2']
# print('append' in dir(seats))      # True: seats can use append()
# print('append' in list.__dict__)   # True: the list class stores it
#
# # seats.label = 'balcony'  # crashes on purpose: AttributeError: 'list' object has no attribute 'label'


# # ---------- Check for understanding ----------
# # For each expression, name the places Python searches, in order, and the place where the search stops.
# # Then run the section to confirm the values. The last line crashes on purpose: comment it out again before you go on.

# coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
#
# print(jazz.performer)       # 1
# print(jazz.ticket_price())  # 2
# print(jazz.__repr__())      # 3
# print(jazz.__ne__(coco))    # 4
# print(jazz.blah)            # 5
