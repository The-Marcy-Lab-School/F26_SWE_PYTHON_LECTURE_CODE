# The Problem a Class Solves: keeping related data together, along with the rules about it.
# Uncomment one section at a time as the lesson goes on.

# ---------- Parallel Lists Drift Apart ----------
names = ['Movie Night: Coco', 'Friday Night Jazz', 'Intro to Pottery']
capacities = [30, 40, 2]
seats_sold = [5, 12, 2]


def seats_left(i):
    return capacities[i] - seats_sold[i]


print(f'{names[1]}: {seats_left(1)} seats left')
# Friday Night Jazz: 28 seats left

names.sort()  # sorts the names but not the capacities or seats_sold

print(f'{names[1]}: {seats_left(1)} seats left')
# Intro to Pottery: 28 seats left -- but the workshop is sold out


# # ---------- Dictionaries Keep the Data Together but Not the Rules ----------
# # Each event's data lives in one record, but the rule lives in separate functions.

# def make_event(name, capacity):
#     return {'name': name, 'capacity': capacity, 'seats_sold': 0}
#
#
# def seats_left(event):
#     return event['capacity'] - event['seats_sold']
#
#
# def sell_ticket(event):
#     if seats_left(event) == 0:
#         print(f"{event['name']} is sold out.")
#         return
#     event['seats_sold'] += 1
#
#
# pottery = make_event('Intro to Pottery', 2)
# sell_ticket(pottery)
# sell_ticket(pottery)
# sell_ticket(pottery)    # Intro to Pottery is sold out.
#
# # # Nothing connects the dictionary to sell_ticket(), so any line can change the record directly:
# pottery['seats_sold'] += 1
# print(seats_left(pottery))    # -1
