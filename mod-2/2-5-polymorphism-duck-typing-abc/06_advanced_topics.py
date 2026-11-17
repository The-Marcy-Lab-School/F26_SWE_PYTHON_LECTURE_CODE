# Advanced Topics

# ---------- raise NotImplementedError ----------
# Raising NotImplementedError in the base class still finds a missing method only when it is called.
class OldEvent:
    def ticket_price(self):
        raise NotImplementedError('Each kind of event must define ticket_price().')


class OldFestival(OldEvent):
    pass


fest = OldFestival()   # created without complaint
# fest.ticket_price()  # crashes on purpose: NotImplementedError: Each kind of event must define ticket_price().
