# Design

## 1. The stakeholder's problem

Riverside Community Hall sells tickets for its concerts, workshops, and movie nights on a paper sign-up sheet at the front desk. Popular workshops end up with too many sign-ups than available seats, and the staff at the door cannot tell who has paid, who has already checked in, or whether a refund request is still allowed.

## 2. UML class diagram

`+` marks a public attribute or method and `-` marks a non-public one (one whose name begins with `_`).

```
Venue
------------------------------------------------------------
+ name
- _events             list of Event
- _attendees          dictionary of email -> Attendee
- _reservations       list of Reservation
- _next_number        the number the next reservation will get
------------------------------------------------------------
+ events, attendees, reservations    (read-only copies)
+ is_valid_email(email)              (static method)
+ add_event(event)
+ add_attendee(attendee)
+ find_attendee(email)
+ find_events(matches)
+ upcoming_events(today)
+ seats_left(event)
+ find_reservation(number)
+ reservations_for(attendee)
+ book(attendee, event, today)
+ refund(reservation, today)


Event
------------------------------------------------------------
+ name
+ date
- _capacity           read and changed through capacity
- _base_price         read and changed through base_price
------------------------------------------------------------
+ ticket_price()
+ can_refund(today)
        ^
        | is an Event
        |
        +-- Concert     + performer       + ticket_price()   + can_refund(today)
        +-- Workshop    + materials_fee   + ticket_price()   + can_refund(today)
        +-- Screening                                        + can_refund(today)


Reservation
------------------------------------------------------------
+ number
+ attendee
+ event
+ price
- _status             read through status, changed only by the methods below
------------------------------------------------------------
+ is_active()
+ pay()               requires reserved
+ check_in()          requires paid
+ refund()            requires paid


Attendee  (dataclass)
------------------------------------------------------------
+ name
+ email


Relationships

Venue ------holds many-----> Event
Venue ------holds many-----> Attendee
Venue ------holds many-----> Reservation
Reservation --refers to one--> Attendee
Reservation --refers to one--> Event
```

## 3. What each class owns

| Class       | Owns                                                                | Can do                                                                                       |
| ----------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Venue       | Every event, attendee, and reservation                              | Add events and attendees, search them, book a ticket, refund a reservation, count seats left |
| Event       | A name, a date, a capacity, and a base price                        | Say what a ticket costs and whether a ticket can still be refunded on a given day            |
| Concert     | Everything an Event owns, plus the performer                        | Add a service fee to the price, and close refunds one week before the show                   |
| Workshop    | Everything an Event owns, plus a materials fee                      | Add the materials fee to the price, and close refunds two days before                        |
| Screening   | Everything an Event owns                                            | Refuse every refund                                                                          |
| Reservation | Its number, its attendee, its event, the price agreed, and a status | Move from reserved to paid, from paid to checked in, or from paid to refunded                |
| Attendee    | A name and an email address                                         | Nothing beyond holding its data                                                              |

## 4. Relationships

- **Venue to Event, Attendee, and Reservation: one-way.** The venue holds all three collections so that one class can check every rule that involves more than one object. None of them needs to know about the venue.
- **Reservation to Attendee: one-way.** A reservation needs to know whose it is. An attendee does not hold a list of reservations, because the venue can find them with `reservations_for()`, and keeping one list means there is only one place to keep up to date.
- **Reservation to Event: one-way.** A reservation needs its event to know its price and its refund rule. An event does not hold its reservations. The venue counts them in `seats_left()`, for the same reason as above.
- **Concert, Workshop, and Screening to Event: inheritance.** Each one is an Event, so each inherits everything an Event owns and changes only what is different about it.

## 5. Design strategies and the higher-order function

| Strategy               | Class       | How it meets the count                                                                                                                   |
| ---------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Coordinator            | Venue       | Stores three collections. Refuses an event already on the calendar, a booking for a sold-out event or a past event, and a refund once the refund window has closed |
| Status-Driven Behavior | Reservation | Holds a `_status`. `pay()` refuses unless the reservation is reserved, and `check_in()` and `refund()` refuse unless it is paid          |
| Intermediary Object    | Reservation | Refers to an Attendee and an Event, and holds the price, which belongs to that pairing rather than to either one                         |

Higher-order function:

Both forms appear. The decorators `@requires_reserved` and `@requires_paid` guard the reservation's status changes, so the status check is written once instead of at the top of every method that needs it. `Venue.find_events()` takes a function as a parameter, so one method can answer any question about the events: which are upcoming, which are cheap, which have a given name.

Shared contract for the polymorphic loop — the method names every kind of event defines:

- `ticket_price()`
- `can_refund(today)`

## 6. One design decision I struggled with

Which class should enforce the refund window? The window depends on the kind of event and on today's date. It could have gone inside `Reservation.refund()`, which would mean `refund()` takes today's date as an argument. Or it could go in the venue, which checks the window and then asks the reservation to change its status.

I put it in the venue. Every other method on Reservation checks only the reservation's own status, so keeping the date out of `refund()` keeps that class about one thing. It also means each status guard's wrapper only has to accept `self`. The cost is that code which calls `reservation.refund()` directly, without going through the venue, skips the date check, so the menu always refunds through `venue.refund()`.

## 7. What I would change if I started again

The statuses are plain strings, such as `'reserved'` and `'paid'`, so a misspelled status anywhere in the code would go unnoticed, which is the same kind of bug this design set out to prevent. I would store each status in one named constant and use the constant everywhere. I would also consider making Event an abstract base class, so that a new kind of event that forgets `can_refund()` is refused when it is created. `src/events_abc.py` shows that version.
