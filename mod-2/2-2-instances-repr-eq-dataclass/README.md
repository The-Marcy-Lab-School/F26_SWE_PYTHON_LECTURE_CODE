# 2.2 Composition, `__repr__`, `__eq__`, and `@dataclass`

Every file in this folder follows one part of the lesson, and most of them use the lesson's `Event` and `Venue` classes. Run any file with `python3`, for example:

```sh
python3 01_objects_that_hold_other_objects.py
```

The lesson's case study checks use the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_objects_that_hold_other_objects.py` | Objects That Hold Other Objects: Reaching Through One Object to Another, and A Method That Searches the List |
| `02_events_by_month.py` | Challenge: Events by Month |
| `03_printing_with_repr.py` | Printing an Instance with `__repr__` |
| `04_comparing_with_eq.py` | Comparing Instances with `__eq__` |
| `05_performer.py` | Challenge: A Readable Performer, Challenge: Equal Performers, and Challenge: Refactor Performer with `@dataclass` |
| `06_writing_less_with_dataclass.py` | Writing Less with `@dataclass` |
| `07_reservations.py` | Putting It Together: Reservations |
| `08_one_ticket_per_attendee.py` | Challenge: One Ticket per Attendee |
| `09_advanced_topics.py` | Advanced Topics |
| `events-practice/` | Testing That a Venue Refuses a Duplicate |

Each numbered file starts with code that runs as it is. Below it, the rest of the file is commented out in sections named after the lesson's headings. As the lesson goes on, uncomment one section at a time and run the file again. In VS Code, select the whole section, from its `# # ----------` heading to its last line, and press `Command+/` (`Ctrl+/` on Windows). The headings and explanations are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. Several lines end with `# crashes on purpose`. Uncomment one to see the error, then comment it out again so the rest of the file still runs.

## The Challenges

`02_events_by_month.py`, `05_performer.py`, and `08_one_ticket_per_attendee.py` each hold a class with its method names written for you. Each file runs before you start, and the comments beside the `print()` calls say what each one should print when you are done.

`05_performer.py` holds three challenges that build one `Performer` class: add `__repr__`, then `__eq__`, then rewrite the class with `@dataclass` and check that the output still matches.

## Testing That a Venue Refuses a Duplicate

`events-practice/` is a small project set up the way every Mod 2 repository is: the classes in `src/venue.py`, the tests in `tests/test_venue.py`, and a `pytest.ini` that tells pytest where to find both. Run the tests from inside the folder, with your virtual environment turned on and pytest installed:

```sh
cd events-practice
pytest
```

Both tests pass. For the lesson's "Predict, then run", delete the `__eq__` method from `Event` in `src/venue.py`, run `pytest` again, and read which test fails. Put the `__eq__` method back afterwards.
