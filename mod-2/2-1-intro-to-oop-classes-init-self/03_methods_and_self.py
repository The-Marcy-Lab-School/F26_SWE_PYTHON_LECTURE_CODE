# Methods and self: a method is a function defined inside a class.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


# ---------- Writing a Method ----------
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


pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
pottery.sell_ticket()
pottery.sell_ticket()
pottery.sell_ticket()        # Intro to Pottery is sold out.
print(pottery.seats_left())  # 0


# # ---------- self Is the Value Before the Dot ----------
# # Python finds the method in the value's class and calls it with the value as the first argument.

# print(str.upper('hello'))    # called on the class str, with 'hello' as the argument -> HELLO
# print('hello'.upper())       # called on the string instance with no argument -> HELLO
#
# # # The same rule holds for the classes you write: the instance is passed in as self.
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
#
# print(jazz.seats_left())
# # finds the Event.seats_left method and invokes it with jazz as the self argument -> 40
#
# print(Event.seats_left(jazz))
# # invokes the method on the class directly, passing in jazz as self -> 40
#
# # # A method defined without a parameter for self fails as soon as it is called:
# class BrokenEvent:
#     def __init__(self, name, capacity):
#         self.name = name
#         self.capacity = capacity
#
#     def seats_left():
#         return 0
#
#
# broken = BrokenEvent('Friday Night Jazz', 40)
# # broken.seats_left()  # crashes on purpose: TypeError: BrokenEvent.seats_left() takes 0 positional arguments but 1 was given
#
# # # Predict, then run: what does this print?
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# pottery = Event('Intro to Pottery', date(2026, 11, 20), 2)
#
# pottery.sell_ticket()
# pottery.sell_ticket()
#
# print(pottery.seats_left())
# print(jazz.seats_left())


# # ---------- A Method That Takes Arguments ----------
# # The instance still arrives first, and the arguments you write come after it.

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
# jazz = Event('Friday Night Jazz', date(2026, 12, 5), 40)
# today = date(2026, 11, 12)
#
# print(jazz.can_refund(today))          # True
# print(Event.can_refund(jazz, today))   # True
