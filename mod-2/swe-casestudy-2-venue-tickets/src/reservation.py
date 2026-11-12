"""A reservation connects one attendee to one event.

A reservation moves through these statuses:
    reserved -> paid -> checked_in
                paid -> refunded
"""


# Each decorator below guards a method that may only run from one status.
# The wrapper replaces the method, so calling reservation.check_in() runs the
# wrapper first. If the status is wrong, the wrapper prints why and returns
# before the original method can run.

def requires_reserved(method):
    def wrapper(self):
        if self.status != 'reserved':
            print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
            return
        return method(self)
    return wrapper


def requires_paid(method):
    def wrapper(self):
        if self.status != 'paid':
            print(f'Cannot {method.__name__}: reservation #{self.number} is {self.status}.')
            return
        return method(self)
    return wrapper


class Reservation:
    def __init__(self, number, attendee, event):
        self.number = number
        self.attendee = attendee
        self.event = event
        # The price belongs to this pairing of attendee and event. It is copied
        # now, so a later change to the event's price does not change what this
        # attendee agreed to pay.
        self.price = event.ticket_price()
        self._status = 'reserved'

    # status has a getter and no setter. Assigning to reservation.status raises
    # an error, so the status can only change through the methods below, and
    # their guards run every time.
    @property
    def status(self):
        return self._status

    def is_active(self):
        return self._status != 'refunded'

    @requires_reserved
    def pay(self):
        self._status = 'paid'

    @requires_paid
    def check_in(self):
        self._status = 'checked_in'

    @requires_paid
    def refund(self):
        self._status = 'refunded'

    def __repr__(self):
        return f'Reservation(#{self.number}, {self.attendee.name!r}, {self.event.name!r}, {self.status!r})'
