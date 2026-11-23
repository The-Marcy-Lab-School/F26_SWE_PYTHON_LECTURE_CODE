# Reading a Decorator Factory: requires_status() takes the required status and builds a decorator from it.
# Uncomment one section at a time as the lesson goes on.


def requires_status(status):        # the factory: takes the required status
    def decorator(method):          # the decorator the factory builds and returns
        def wrapper(self):          # closes over both status and method
            if self.status != status:
                print(f'Reservation must be {status} in order to use {method.__name__}.')
                return
            return method(self)
        return wrapper
    return decorator


class Reservation:
    def __init__(self, number, attendee_name):
        self.number = number
        self.attendee_name = attendee_name
        self._status = 'reserved'

    @property
    def status(self):
        return self._status

    @requires_status('reserved')    # calls the factory, then applies the decorator it returns
    def pay(self):
        self._status = 'paid'

    @requires_status('paid')
    def check_in(self):
        self._status = 'checked_in'

    @requires_status('paid')
    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.check_in()          # Reservation must be paid in order to use check_in.
maya.pay()
maya.pay()               # Reservation must be reserved in order to use pay.
maya.check_in()
print(maya.status)       # checked_in


# # ---------- Check for understanding ----------
# # When Python reaches @requires_status('paid') above def check_in, what are the two steps it performs?
# # Name the call that builds the decorator and the function that the decorator then wraps.
# # Then predict what the line below shows, and why.

# print(requires_status('paid'))
