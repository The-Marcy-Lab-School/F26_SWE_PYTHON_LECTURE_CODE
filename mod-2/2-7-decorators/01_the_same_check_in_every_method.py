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
            print('Reservation must be reserved in order to use pay.')
            return
        self._status = 'paid'

    def check_in(self):
        if self._status != 'paid':
            print('Reservation must be paid in order to use check_in.')
            return
        self._status = 'checked_in'

    def refund(self):
        self._status = 'refunded'


maya = Reservation(1001, 'Maya Rodriguez')
maya.check_in()          # Reservation must be paid in order to use check_in.
maya.refund()
print(maya.status)       # refunded


# # ---------- Q: What is expected about this behavior? What is unexpected? ----------
# # Maya has not paid. Which of the two calls above did what you expected, and which did not?


# # ---------- Q: Which lines are the same in pay() and check_in(), and which are different? ----------
# # Compare the two methods line by line before reading on.
