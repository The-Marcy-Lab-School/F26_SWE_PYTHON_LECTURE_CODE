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
    def __init__(self, number, attendee_name):
        self.number = number
        self.attendee_name = attendee_name
        self._status = 'reserved'

    @property
    def status(self):
        return self._status

    @requires_reserved
    def pay(self):
        self._status = 'paid'

    @requires_paid
    def check_in(self):
        self._status = 'checked_in'

    @requires_paid
    def refund(self):
        self._status = 'refunded'
