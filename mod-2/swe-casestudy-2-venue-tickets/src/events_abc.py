"""The same events as events.py, with Event written as an abstract base class.

The application does not use this file. It shows what changes when Event becomes
an abstract base class (ABC): Python refuses to create an Event itself, and it
refuses to create any kind of event that does not define both ticket_price() and
can_refund().

To swap it into the application, change the import at the top of sample_data.py from
    from events import Concert, Workshop, Screening
to
    from events_abc import Concert, Workshop, Screening
and run the application. Nothing else changes, because the rest of the code only
calls methods that every kind of event answers.

To see the refusal, run this file on its own:
    python3 src/events_abc.py
"""

from abc import ABC, abstractmethod
from datetime import date, timedelta


class Event(ABC):
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

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

    # @abstractmethod means every subclass must define this method. An abstract
    # method can still have a body, and a subclass can reach it with super().
    @abstractmethod
    def ticket_price(self):
        return self.base_price

    @abstractmethod
    def can_refund(self, today):
        """Return True if a ticket can still be refunded on the given day."""

    def __repr__(self):
        return f'{type(self).__name__}({self.name!r}, {self.date})'

    # Two Event objects describe the same event when they share a name and a
    # date, so the venue can find an event it already has with `in`
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
        return today <= self.date - timedelta(days=2)


class Screening(Event):
    # In events.py, Screening inherits ticket_price() without defining it. Here
    # ticket_price() is abstract, so Screening must define it, even though it
    # only uses the parent's version.
    def ticket_price(self):
        return super().ticket_price()

    def can_refund(self, today):
        return False


if __name__ == "__main__":
    # A kind of event that forgot to define can_refund()
    class Festival(Event):
        def ticket_price(self):
            return super().ticket_price()

    try:
        Festival('Summer Festival', date.today(), 500, 40)
    except TypeError as error:
        print(f'Python refused to create a Festival: {error}')
