# A Decorator That Refuses: requires_paid checks the status before the method runs, and refuses from any other status.
# Uncomment one section at a time as the lesson goes on.


def requires_paid(method):
    def wrapper(self):                      # receives the instance as self, as the method would
        if self.status != 'paid':
            # method.__name__ is the name of the method being refused, such as 'refund'
            print(f'Reservation must be paid in order to use {method.__name__}.')
            return                          # refuses: the method's body never runs
        return method(self)                 # allowed: runs the original method
    return wrapper


# Challenge: @requires_reserved
# Finish this decorator so that it refuses a call unless the reservation is reserved.
# Then put @requires_reserved above pay() and delete the guard clause inside pay(),
# so that pay() contains only the line that changes the status.
def requires_reserved(method):
    return method


class Reservation:
    def __init__(self, number, attendee_name):
        self.number = number
        self.attendee_name = attendee_name
        self._status = 'reserved'

    @property
    def status(self):
        return self._status

    def pay(self):
        if self._status != 'reserved':
            print('Reservation must be reserved in order to use pay.')
            return
        self._status = 'paid'

    @requires_paid      # check_in() runs only when the reservation is paid
    def check_in(self):
        self._status = 'checked_in'

    @requires_paid      # one decorator guards a second method
    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.refund()            # Reservation must be paid in order to use refund.
print(maya.status)       # reserved

maya.pay()
maya.refund()
print(maya.status)       # refunded


# # ---------- Check for understanding ----------
# # In requires_paid, which variable does wrapper close over? requires_paid returned long before
# # maya.check_in() is called, so how can wrapper still call the original check_in?


# # ---------- Challenge: @requires_reserved ----------
# # Finish requires_reserved near the top of this file and use it on pay(). These lines print the same
# # thing before and after your change, because pay() refuses by hand until you replace its guard clause.

sam = Reservation(1002, 'Sam Lee')
sam.pay()
# sam.pay()                # Reservation must be reserved in order to use pay.
# print(sam.status)        # paid


# # ---------- Check for understanding ----------
# # Open src/reservation.py in the case study. Which methods does each decorator guard?
# # Suppose reservation #1005 is reserved and the program calls its refund() method. What does the program
# # print, what happens to the status, and why does the message use method.__name__ instead of the word refund?
