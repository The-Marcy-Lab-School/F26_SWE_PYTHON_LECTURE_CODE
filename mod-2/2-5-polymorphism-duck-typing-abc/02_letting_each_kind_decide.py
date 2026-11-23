# Letting Each Kind of Event Decide: each class holds its own version of each rule, so the loop never asks which kind it has.
# Uncomment one section at a time as the lesson goes on.

from datetime import date, timedelta


# ---------- Letting Each Kind of Event Decide ----------
class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    # Standard pricing for all events unless overridden
    def ticket_price(self):
        return self.base_price

    # Standard refund policy for all events unless overridden
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


class Workshop(Event):
    def __init__(self, name, date, capacity, base_price, materials_fee):
        super().__init__(name, date, capacity, base_price)
        self.materials_fee = materials_fee

    def ticket_price(self):
        return super().ticket_price() + self.materials_fee

    def can_refund(self, today):
        return today <= self.date - timedelta(days=2)


class Screening(Event):
    def can_refund(self, today):
        return False


jazz = Concert('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25, performer='The Blue Notes')
pottery = Workshop('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15, materials_fee=10)
coco = Screening('Movie Night: Coco', date(2026, 12, 18), capacity=30, base_price=8)
events = [jazz, pottery, coco]

# today is 4 days before the concert, 8 before the workshop
today = date(2026, 12, 1)

for event in events:
    price = event.ticket_price()
    marker = ' (refundable)' if event.can_refund(today) else ''
    print(f'{event.name}: ${price}{marker}')
# Friday Night Jazz: $30
# Intro to Pottery: $25 (refundable)
# Movie Night: Coco: $8

print(len('Coco'), len(['A1', 'A2']), len({'jazz': 30}))   # 4 2 1


# # ---------- Predict, then run ----------
# # The venue adds guided tours again: the base price plus a $3 booking fee, refundable until the day before.
# # This time Tour defines its own ticket_price() and reuses Event's can_refund(). What does the loop print?

class Tour(Event):
    BOOKING_FEE = 3

    def ticket_price(self):
        return super().ticket_price() + Tour.BOOKING_FEE


harbor = Tour('Harbor History Walk', date(2026, 12, 12), capacity=15, base_price=20)
events.append(harbor)

# for event in events:
#     price = event.ticket_price()
#     marker = ' (refundable)' if event.can_refund(today) else ''
#     print(f'{event.name}: ${price}{marker}')


# # ---------- Q: How does this example show polymorphism? ----------

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print('Vrooom')


class RaceCar(Car):
    def drive(self):
        print('Vah... Vah...')
        super().drive()
        print('WHEEEEEEE!!!!')


cars = [Car('Chevy', 'Cobalt'), RaceCar('Ferrari', 'Portofino'), Car('Tesla', 'Model X')]
# for car in cars:
#     car.drive()
# # Vrooom
# # Vah... Vah...
# # Vrooom
# # WHEEEEEEE!!!!
# # Vrooom
