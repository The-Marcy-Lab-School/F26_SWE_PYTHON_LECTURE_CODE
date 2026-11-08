# ---------- Challenge: Room Rentals 🏗️🏗️🏗️🏗️🏗️ ----------
# Riverside Community Hall also rents out its rooms. Finish the Room class:
# - __init__ stores the room's name, its number of seats, and its hourly rate in dollars on the instance.
# - cost(hours) returns what renting the room for that many hours costs.
# - fits(group_size) returns True when a group of that size has enough seats, and False otherwise.
# Then rewrite one of the method calls at the bottom in the form Room.cost(...).
# Run the file after each step. It runs before you start, and prints None until each method is done:
#     python3 04_room_rentals.py


class Room:
    def __init__(self, name, seats, hourly_rate):
        pass  # store all three on self

    def cost(self, hours):
        return None  # replace with the cost of renting the room for this many hours

    def fits(self, group_size):
        return None  # replace with True or False


studio = Room('Dance Studio', 25, 40)
hall = Room('Main Hall', 200, 150)

print(studio.cost(3))     # should print 120
print(hall.fits(180))     # should print True
print(studio.fits(30))    # should print False
