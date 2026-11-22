# Duck Typing: code that calls a method works with any object that defines it, whether or not its class inherits from Event.
# Uncomment one section at a time as the lesson goes on.

from datetime import date, timedelta


# The classes from Letting Each Kind of Event Decide
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
coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
today = date(2026, 12, 1)


# ---------- Unrelated Classes Can Define the Same Method ----------
# len() calls its argument's __len__ without checking the argument's type.
print(len(['A1', 'A2']))   # 2: list defines __len__
print(len('Coco'))         # 4: str defines __len__


class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)


my_playlist = Playlist(['Song A', 'Song B', 'Song C'])
print(len(my_playlist))    # 3: Playlist defines __len__, and inherits from neither list nor str


# # ---------- Checking the Class or Duck Typing ----------
# # MuseumTour was written by another team and does not inherit from Event, but it defines both methods the menu calls.

class MuseumTour:
    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

    def ticket_price(self):
        return self.price

    def can_refund(self, today):
        return today < self.date


gallery = MuseumTour('Gallery After Dark', date(2026, 12, 11), price=12)
menu = [jazz, coco, gallery]

# # Checking the class: the museum tour is skipped, even though it has both methods
# for item in menu:
#     if isinstance(item, Event):
#         price = item.ticket_price()
#         marker = ' (refundable)' if item.can_refund(today) else ''
#         print(f'{item.name}: ${price}{marker}')
# # Friday Night Jazz: $30
# # Movie Night: Coco: $8
#
# # Duck typing: every item that has both methods works
# for item in menu:
#     price = item.ticket_price()
#     marker = ' (refundable)' if item.can_refund(today) else ''
#     print(f'{item.name}: ${price}{marker}')
# # Friday Night Jazz: $30
# # Movie Night: Coco: $8
# # Gallery After Dark: $12 (refundable)


# # ---------- Predict, then run ----------
# # A botanical garden sends its own class, GardenTour. It defines ticket_price() but not can_refund().
# # What does the menu loop print? This one ends in an error: comment those lines out again before you go on.

class GardenTour:
    def __init__(self, name, date, price):
        self.name = name
        self.date = date
        self.price = price

    def ticket_price(self):
        return self.price


lanterns = GardenTour('Lantern Walk', date(2026, 12, 14), price=10)
menu = [jazz, gallery, lanterns, coco]

# for item in menu:
#     price = item.ticket_price()
#     marker = ' (refundable)' if item.can_refund(today) else ''
#     print(f'{item.name}: ${price}{marker}')


# # ---------- Q: Does this code use inheritance? Does it show polymorphism? ----------

class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} said woof')


class Cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f'{self.name} said meow')


# for animal in [Dog('Snoopy'), Cat('Garfield')]:
#     animal.speak()
# # Snoopy said woof
# # Garfield said meow
