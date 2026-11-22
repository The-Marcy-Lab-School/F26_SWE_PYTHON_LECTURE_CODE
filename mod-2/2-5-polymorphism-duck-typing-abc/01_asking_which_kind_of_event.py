# Asking Which Kind of Event: the rules for prices and refunds live in two functions outside the classes,
# and each function asks which kind of event it was given with isinstance().
# Uncomment one section at a time as the lesson goes on.

from datetime import date, timedelta


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price


# Same as Event with a performer
class Concert(Event):
    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer


# Same as Event with a materials fee
class Workshop(Event):
    def __init__(self, name, date, capacity, base_price, materials_fee):
        super().__init__(name, date, capacity, base_price)
        self.materials_fee = materials_fee


# Exact same as Event
class Screening(Event):
    pass


# One branch for each kind of event
def ticket_price(event):
    if isinstance(event, Concert):
        return event.base_price + 5
    elif isinstance(event, Workshop):
        return event.base_price + event.materials_fee
    else:
        return event.base_price


# One branch for each kind of event
def can_refund(event, today):
    if isinstance(event, Concert):
        # Can be refunded up to 7 days before
        return today <= event.date - timedelta(days=7)
    elif isinstance(event, Workshop):
        # Can be refunded up to 2 days before
        return today <= event.date - timedelta(days=2)
    else:
        # All other events cannot be refunded
        return False


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
pottery = Workshop('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15, materials_fee=10)
coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)

# today is 4 days before the concert, 8 before the workshop
today = date(2026, 12, 1)

for event in [jazz, pottery, coco]:
    price = ticket_price(event)
    marker = ' (refundable)' if can_refund(event, today) else ''
    print(f'{event.name}: ${price}{marker}')

# Friday Night Jazz: $30
# Intro to Pottery: $25 (refundable)
# Movie Night: Coco: $8


# # ---------- Q: The venue adds guided tours ----------
# # A guided tour charges its base price plus a $3 booking fee, and its tickets can be refunded until the day before.
# # Tour is added as a subclass, and nobody edits the two functions. What do the two print() calls show?

class Tour(Event):
    BOOKING_FEE = 3


harbor = Tour('Harbor History Walk', date(2026, 12, 12), capacity=15, base_price=20)
# print(ticket_price(harbor))
# print(can_refund(harbor, date(2026, 12, 1)))
