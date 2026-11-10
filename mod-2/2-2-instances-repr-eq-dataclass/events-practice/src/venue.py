class Event:
    def __init__(self, name, date, capacity):
        self.name = name
        self.date = date
        self.capacity = capacity

    def __repr__(self):
        return f'Event({self.name!r}, {self.date})'

    def __eq__(self, other):
        return self.name == other.name and self.date == other.date


class Venue:
    def __init__(self, name):
        self.name = name
        self.events = []

    def add_event(self, event):
        if event in self.events:
            print(f'{event.name} on {event.date} is already on the calendar.')
            return
        self.events.append(event)
