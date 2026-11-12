"""The events the venue hosts.

Event holds what every event has. Concert, Workshop, and Screening are the three
kinds of event, and each one answers ticket_price() and can_refund() in its own way.
"""

from datetime import timedelta


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        # These two assignments run the setters below, so an invalid value is
        # refused even when the event is first created
        self.capacity = capacity
        self.base_price = base_price

    # A capacity below 1 would break the seat count, so the value is stored in
    # _capacity and every change goes through the setter, which refuses it
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if value < 1:
            raise ValueError(f'Capacity must be at least 1, not {value}.')
        self._capacity = value

    @property
    def base_price(self):
        return self._base_price

    @base_price.setter
    def base_price(self, value):
        if value < 0:
            raise ValueError(f'A price cannot be negative, not {value}.')
        self._base_price = value

    def ticket_price(self):
        return self.base_price

    def can_refund(self, today):
        # By default, a ticket can be refunded on any day before the event
        return today < self.date

    def __repr__(self):
        # type(self).__name__ is the name of the object's class, so a Concert
        # prints as Concert(...) without Concert defining its own __repr__
        return f'{type(self).__name__}({self.name!r}, {self.date})'

    # Two Event objects describe the same event when they share a name and a
    # date, so the venue can find an event it already has with `in`
    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Concert(Event):
    # A class attribute: one service fee shared by every concert
    SERVICE_FEE = 5

    def __init__(self, name, date, capacity, base_price, performer):
        super().__init__(name, date, capacity, base_price)
        self.performer = performer

    def ticket_price(self):
        # Extends the parent's version rather than replacing it
        return super().ticket_price() + Concert.SERVICE_FEE

    def can_refund(self, today):
        # Concert refunds close one week before the show
        return today <= self.date - timedelta(days=7)


class Workshop(Event):
    def __init__(self, name, date, capacity, base_price, materials_fee):
        super().__init__(name, date, capacity, base_price)
        # Something is missing here. Compare how this class stores materials_fee
        # with how Event stores capacity and base_price. What would happen to a
        # workshop's ticket price if this value were wrong, and how would you
        # change the class so that it could not be?
        self.materials_fee = materials_fee

    def ticket_price(self):
        return super().ticket_price() + self.materials_fee

    def can_refund(self, today):
        # Workshop refunds close two days before, so the instructor can buy materials
        return today <= self.date - timedelta(days=2)


class Screening(Event):
    # A Screening uses Event's ticket_price() unchanged, so it does not define one

    def can_refund(self, today):
        # Screening tickets are cheap and are never refunded
        return False
