# Functions That Return Functions: an outer function builds a test and hands it back without calling it.
# Uncomment one section at a time as the lesson goes on.

from datetime import date


class Event:
    def __init__(self, name, date, capacity, base_price):
        self.name = name
        self.date = date
        self.capacity = capacity
        self.base_price = base_price

    def ticket_price(self):
        return self.base_price

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'


# The venue from Passing a Function to a Function: one search method that takes the test as a parameter
class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def find_events(self, matches):
        return [event for event in self.events if matches(event)]


hall = Venue('Riverside Community Hall')
hall.add_event(Event('Friday Night Jazz', date(2026, 12, 5), capacity=40, base_price=25))
hall.add_event(Event('Intro to Pottery', date(2026, 12, 9), capacity=12, base_price=15))
hall.add_event(Event('Movie Night: Coco', date(2026, 11, 28), capacity=30, base_price=8))
hall.add_event(Event('Board Game Night', date(2027, 1, 8), capacity=25, base_price=0))


def matches_month(month):
    def matches(event):
        return event.date.month == month
    return matches


in_december = matches_month(12)
print(in_december)                          # <function matches_month.<locals>.matches at 0x...>
print(hall.find_events(in_december))        # [Event('Friday Night Jazz', 2026-12-05), Event('Intro to Pottery', 2026-12-09)]
print(hall.find_events(matches_month(1)))   # [Event('Board Game Night', 2027-01-08)]


# # ---------- Predict, then run ----------
# # Someone changes the last line of matches_month() from return matches to return matches().
# # What happens when the program calls matches_month(12)?
# # Uncomment the last line on its own and run the file. Then comment it out again.

def matches_month(month):
    def matches(event):
        return event.date.month == month
    return matches()


# # in_december = matches_month(12)   # crashes on purpose


# # ---------- Check for understanding ----------
# # For each function below, say whether it is a higher-order function, and if it is, which condition it meets.
# # 1. sorted(), called as sorted(hall.events, key=lambda event: event.date)
# # 2. matches_month
# # 3. in_december, the function that matches_month(12) returned

def matches_month(month):
    def matches(event):
        return event.date.month == month
    return matches


in_december = matches_month(12)
# print(in_december(hall.events[0]))   # True: in_december receives one event and returns True or False


# # ---------- Closures ----------
# # announce closes over venue_name, and keeps it after make_announcer() has returned.

def make_announcer(venue_name):
    def announce(message):
        print(f'{venue_name}: {message}')
    return announce


main_hall = make_announcer('Riverside Community Hall')
# main_hall('Doors open at 7.')     # Riverside Community Hall: Doors open at 7.
#
# # print(month)   # crashes on purpose


# # ---------- Q: Which is the outer function, which is the inner function, and which variable does the inner one refer to? ----------

def sort_by_distance_from(prices, target):
    return sorted(prices, key=lambda price: abs(price - target))


# print(sort_by_distance_from([8, 30, 25, 15], 20))   # [25, 15, 30, 8]


# # ---------- Predict, then run ----------
# # The venue also announces events in its annex. What do the three calls print?

main_hall = make_announcer('Riverside Community Hall')
annex = make_announcer('Riverside Annex')

# main_hall('Doors open at 7.')
# annex('Doors open at 8.')
# main_hall('Last call.')


# # ---------- Check for understanding ----------
# # Open src/venue.py in the case study and find upcoming_events(). For each lambda in it, say which function
# # calls it, what it receives, and what it returns. Which variable does the first lambda close over?

# # def upcoming_events(self, today):
# #     upcoming = self.find_events(lambda event: event.date >= today)
# #     return sorted(upcoming, key=lambda event: event.date)
