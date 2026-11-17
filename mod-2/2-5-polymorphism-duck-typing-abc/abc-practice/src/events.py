from abc import ABC, abstractmethod
from datetime import timedelta


# Contract: every kind of event defines
#   ticket_price()      the price of one ticket
#   can_refund(today)   whether a ticket can still be refunded on that day
class Event(ABC):
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    @abstractmethod
    def ticket_price(self):
        return self.base_price

    @abstractmethod
    def can_refund(self, today):
        pass


class Concert(Event):
    SERVICE_FEE = 5

    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer

    def ticket_price(self):
        return super().ticket_price() + Concert.SERVICE_FEE

    def can_refund(self, today):
        return today <= self.date - timedelta(days=7)
