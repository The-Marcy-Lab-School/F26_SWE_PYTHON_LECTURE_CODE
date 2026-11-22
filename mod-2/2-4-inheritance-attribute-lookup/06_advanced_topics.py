# Advanced Topics
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price


# ---------- Forgetting super().__init__() ----------
# The mistake is in __init__, but the error appears later, on the line that reads jazz.name.
class Concert(Event):
    def __init__(self, name, date, capacity, base_price, performer):
        self.performer = performer      # super().__init__() is missing


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
# print(jazz.name)  # crashes on purpose: AttributeError: 'Concert' object has no attribute 'name'


# # ---------- Assigning a Class Attribute Through an Instance ----------
# # Assigning through an instance creates a new instance attribute. It does not change the class attribute.

class Concert(Event):
    SERVICE_FEE = 5

    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer

    def ticket_price(self):
        return super().ticket_price() + Concert.SERVICE_FEE


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
jazz.SERVICE_FEE = 0

# print(jazz.SERVICE_FEE)      # 0
# print(Concert.SERVICE_FEE)   # 5
# print(jazz.ticket_price())   # 30


# # ---------- isinstance() and type() ----------
# # isinstance() asks whether an object is a kind of something. type() names only the object's own class.

# print(isinstance(jazz, Concert))   # True
# print(isinstance(jazz, Event))     # True
# print(type(jazz) == Concert)       # True
# print(type(jazz) == Event)         # False


# # ---------- __mro__: The Lookup Order Written Down ----------

# print(Concert.__mro__)
# # (<class '__main__.Concert'>, <class '__main__.Event'>, <class 'object'>)


# # ---------- Not Every Object Has a __dict__ ----------
# # dir() works on every object, so use it to explore a value whose class you did not write.

seats = ['A1', 'A2']

# print('append' in dir(seats))   # True
# # print(seats.__dict__)  # crashes on purpose: AttributeError: 'list' object has no attribute '__dict__'
