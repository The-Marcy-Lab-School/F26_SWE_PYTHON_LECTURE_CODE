# ---------- Challenge: Library Loans Without isinstance() 🏗️🏗️🏗️🏗️🏗️ ----------
# A library lends three kinds of item. A book can be borrowed for 21 days and costs $1 for each day it is late.
# A DVD can be borrowed for 7 days and costs $3 for each day it is late.
# A magazine can be borrowed for 14 days and has no late fee.
#
# Refactor the program so that each kind of item decides its own loan period and late fee:
# - move the rules into two methods, loan_days() and late_fee(days_late), and delete the two functions;
# - change the loop to call the methods. It should print the same three lines.
# Then the library starts lending audiobooks, which can be borrowed for 14 days and cost $1 for each day they are late.
# Add an Audiobook class without changing the loop, and add Audiobook('Born a Crime') to the shelf.
# Run the file after each step. It runs before you start:
#     python3 03_library_loans.py


class LibraryItem:
    def __init__(self, title):
        self.title = title


class Book(LibraryItem):
    pass


class DVD(LibraryItem):
    pass


class Magazine(LibraryItem):
    pass


# One branch for each kind of item
def loan_days(item):
    if isinstance(item, Book):
        return 21
    elif isinstance(item, DVD):
        return 7
    else:
        return 14


# One branch for each kind of item
def late_fee(item, days_late):
    if isinstance(item, Book):
        # $1 a day
        return days_late
    elif isinstance(item, DVD):
        # $3 a day
        return days_late * 3
    else:
        # No late fee
        return 0


shelf = [Book('Kindred'), DVD('Spirited Away'), Magazine('National Geographic')]

for item in shelf:
    days = loan_days(item)
    fee = late_fee(item, 4)
    print(f'{item.title}: {days}-day loan, ${fee} if 4 days late')
# Kindred: 21-day loan, $4 if 4 days late
# Spirited Away: 7-day loan, $12 if 4 days late
# National Geographic: 14-day loan, $0 if 4 days late
# Born a Crime: 14-day loan, $4 if 4 days late   <- once Audiobook is on the shelf
