# Project Overview

This project is a command-line ticketing system for Riverside Community Hall, a community venue that hosts concerts, workshops, and movie screenings. Attendees register, book tickets, pay for them, check in at the door, and ask for refunds. The application is built from classes that each own their own data, and it refuses any action that breaks one of the venue's rules, such as booking a sold-out event or checking in before paying.

The design behind the code is written up in [DESIGN.md](DESIGN.md).

## Key Features and Usage Example

After running the application, the user is presented with a menu of options. They can:

1. View upcoming events, with each event's ticket price and the seats left
2. Register as an attendee
3. Book a ticket
4. Pay for a reservation
5. Check in to an event
6. Refund a reservation
7. View their reservations
8. Exit the application

The application starts with sample data, so there is something to explore straight away. The Intro to Pottery workshop starts sold out, and screenings are never refunded, so both refusals can be seen without setting anything up.

In the example below, the user views the upcoming events and then tries to check in to reservation #1002, which has not been paid for yet:

```
Choose an option (1-8): 1
1. Intro to Pottery, Sat Nov 07: $25, 0 of 2 seats left
2. Friday Night Jazz, Sun Nov 15: $30, 39 of 40 seats left
3. Movie Night: Spirited Away, Mon Nov 23: $8, 29 of 30 seats left

Choose an option (1-8): 5
Enter the reservation number: 1002
Cannot check_in: reservation #1002 is reserved.
#1002: Jordan Lee, Intro to Pottery, $25, reserved
```

## Setup

Follow these steps to get started:

```sh
git clone git@github.com:The-Marcy-Lab-School/swe-casestudy-2-venue-tickets.git
cd swe-casestudy-2-venue-tickets

# Create a virtual environment in a folder named .venv, then turn it on
python3 -m venv .venv
source .venv/bin/activate

# Install the packages listed in requirements.txt (pytest and the packages it needs)
pip install -r requirements.txt

# Run the application
python3 src/main.py

# If you need to end the program abruptly, use Control+C
```

Each time you open a new terminal window to work on this project, run `source .venv/bin/activate` again from the project folder. To turn the virtual environment off, run `deactivate`.

## Running Tests

With the virtual environment turned on, run this command from the project folder:

```sh
pytest
```

The `pytest` command finds the test files in the `tests` folder (set by `pytest.ini`) and runs every function whose name begins with `test_`. Those test files can import the classes in the `src` folder (also because of `pytest.ini`).

## The Abstract Base Class Version

`src/events_abc.py` holds the same events as `src/events.py`, with `Event` written as an abstract base class. The application does not use it. To see the abstract base class refuse to create an incomplete kind of event, run:

```sh
python3 src/events_abc.py
```

To run the whole application with it, change the import at the top of `src/sample_data.py` from `from events import ...` to `from events_abc import ...`. Nothing else needs to change.

## Key Technologies and Packages

- Python 3
- Classes, `@property`, `@dataclass`, and `@staticmethod`
- The `datetime` module from the standard library, for event dates
- The `abc` module from the standard library, in `events_abc.py`
- The `os` module from the standard library, to clear the screen
- `pytest`
