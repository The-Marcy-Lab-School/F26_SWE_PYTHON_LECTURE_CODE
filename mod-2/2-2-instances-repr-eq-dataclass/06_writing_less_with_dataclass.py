# Writing Less with @dataclass: Python writes __init__, __repr__, and __eq__ from the attributes you list.
# Uncomment one section at a time as the lesson goes on.

from dataclasses import dataclass


# Every attribute name appears in all three methods
class Seat:
    def __init__(self, section, row, number):
        self.section = section
        self.row = row
        self.number = number

    def __repr__(self):
        return f'Seat(section={self.section!r}, row={self.row!r}, number={self.number!r})'

    def __eq__(self, other):
        return (self.section == other.section
                and self.row == other.row
                and self.number == other.number)


print(Seat('Balcony', 'B', 12))                           # Seat(section='Balcony', row='B', number=12)
print(Seat('Balcony', 'B', 12) == Seat('Balcony', 'B', 12))  # True


# # ---------- The Same Seat with @dataclass ----------
# # Each attribute is listed once, with a type annotation, in the order __init__ takes them.

# @dataclass
# class Seat:
#     section: str
#     row: str
#     number: int
#
#
# front_row = Seat('Balcony', 'B', 12)
# same_seat = Seat('Balcony', 'B', 12)
#
# print(front_row)               # Seat(section='Balcony', row='B', number=12)
# print(front_row == same_seat)  # True
# print(front_row is same_seat)  # False
#
# # # Python does not check the annotations, so a string number is accepted:
# print(Seat('Floor', 'A', '3'))  # Seat(section='Floor', row='A', number='3')
