"""Displays the menu and handles the user's input."""

import os
from datetime import date

from attendee import Attendee


def print_events(venue, events):
    # The same loop works for concerts, workshops, and screenings, because every
    # kind of event answers ticket_price(). The loop never checks which kind it has.
    for i, event in enumerate(events, start=1):
        day = event.date.strftime('%a %b %d')
        print(f'{i}. {event.name}, {day}: ${event.ticket_price()}, '
              f'{venue.seats_left(event)} of {event.capacity} seats left')


def describe(reservation):
    return (f'#{reservation.number}: {reservation.attendee.name}, {reservation.event.name}, '
            f'${reservation.price}, {reservation.status}')


def ask_for_attendee(venue):
    email = input('Enter your email: ').strip()
    attendee = venue.find_attendee(email)
    if attendee is None:
        print(f'No one is registered with {email}. Choose "Register" first.')
    return attendee


def choose_event(venue, today):
    events = venue.upcoming_events(today)
    print_events(venue, events)
    choice = input(f'Choose an event (1-{len(events)}): ').strip()
    try:
        index = int(choice) - 1
    except ValueError:
        print(f'"{choice}" is not a number.')
        return None
    if index < 0 or index >= len(events):
        print(f'{choice} is not one of the events.')
        return None
    return events[index]


def choose_reservation(venue):
    choice = input('Enter the reservation number: ').strip()
    try:
        number = int(choice)
    except ValueError:
        print(f'"{choice}" is not a number.')
        return None
    reservation = venue.find_reservation(number)
    if reservation is None:
        print(f'There is no reservation #{number}.')
    return reservation


def register(venue):
    name = input('Enter your name: ').strip()
    email = input('Enter your email: ').strip()
    try:
        attendee = venue.add_attendee(Attendee(name, email))
    except ValueError as error:
        print(error)
        return
    if attendee is not None:
        print(f'Welcome, {attendee.name}!')


def book_ticket(venue, today):
    attendee = ask_for_attendee(venue)
    if attendee is None:
        return
    event = choose_event(venue, today)
    if event is None:
        return
    reservation = venue.book(attendee, event, today)
    if reservation is not None:
        print(f'Booked! Pay for reservation #{reservation.number} to confirm it.')


# pay(), check_in(), and refund() each print the reservation afterwards, whether
# or not the action was refused, so the user always sees its current status.

def pay(venue):
    reservation = choose_reservation(venue)
    if reservation is None:
        return
    reservation.pay()
    print(describe(reservation))


def check_in(venue):
    reservation = choose_reservation(venue)
    if reservation is None:
        return
    reservation.check_in()
    print(describe(reservation))


def refund(venue, today):
    reservation = choose_reservation(venue)
    if reservation is None:
        return
    venue.refund(reservation, today)
    print(describe(reservation))


def show_reservations(venue):
    attendee = ask_for_attendee(venue)
    if attendee is None:
        return
    reservations = venue.reservations_for(attendee)
    if len(reservations) == 0:
        print('No reservations yet.')
        return
    for reservation in reservations:
        print(describe(reservation))


def show_menu(venue):
    is_running = True
    while is_running:
        today = date.today()

        print(f'\n{venue.name}')
        print('1. View upcoming events')
        print('2. Register')
        print('3. Book a ticket')
        print('4. Pay for a reservation')
        print('5. Check in')
        print('6. Refund a reservation')
        print('7. View your reservations')
        print('8. Exit')

        menu_choice = input('\nChoose an option (1-8): ').strip()

        if menu_choice == '1':
            print_events(venue, venue.upcoming_events(today))
        elif menu_choice == '2':
            register(venue)
        elif menu_choice == '3':
            book_ticket(venue, today)
        elif menu_choice == '4':
            pay(venue)
        elif menu_choice == '5':
            check_in(venue)
        elif menu_choice == '6':
            refund(venue, today)
        elif menu_choice == '7':
            show_reservations(venue)
        elif menu_choice == '8':
            is_running = False
        else:
            print('Invalid option. Please choose 1-8.')

        if is_running:
            input('\nPress Enter to continue...')
            # Clear the output so that the "rounds" of messages don't pile up
            os.system('clear')
