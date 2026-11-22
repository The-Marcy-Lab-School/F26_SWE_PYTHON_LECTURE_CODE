# The Same Check in Every Method: each method that changes the status writes its own guard clause.
# Uncomment one section at a time as the lesson goes on.


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
            print(f'Cannot pay: reservation #{self.number} is {self._status}.')
            return
        self._status = 'paid'

    def check_in(self):
        if self._status != 'paid':
            print(f'Cannot check_in: reservation #{self.number} is {self._status}.')
            return
        self._status = 'checked_in'

    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.check_in()          # Cannot check_in: reservation #1001 is reserved.
maya.refund()
print(maya.status)       # refunded


# # ---------- Q: What is expected about this behavior? What is unexpected? ----------
# # Maya has not paid. Which of the two calls above did what you expected, and which did not?


# # ---------- Q: Which lines are the same in pay() and check_in(), and which are different? ----------
# # Compare the two methods line by line before reading on.
