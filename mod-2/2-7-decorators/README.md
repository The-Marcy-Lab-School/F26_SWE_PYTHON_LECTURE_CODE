# 2.7 Decorators

Every file in this folder follows one part of the lesson, and all of them use the lesson's `Reservation` class and its statuses: reserved, paid, checked in, and refunded. Run any file with `python3`, for example:

```sh
python3 01_the_same_check_in_every_method.py
```

Two of the lesson's checks use the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_the_same_check_in_every_method.py` | The Same Check in Every Method |
| `02_wrapping_a_function.py` | Wrapping a Function, Challenge: Keep the Return Value, and Decorators and the `@` Syntax |
| `03_a_decorator_that_refuses.py` | A Decorator That Refuses, and Challenge: `@requires_reserved` |
| `04_reading_a_decorator_factory.py` | Reading a Decorator Factory |
| `05_advanced_topics.py` | Advanced Topics |
| `guard-practice/` | Testing a Status Guard |

Each numbered file runs as it is. Below the first part, the file is divided into sections named after the lesson's headings. In each section, the definitions and other lines that print nothing are already uncommented, so they run without changing the file's output. The lines that print are commented out. As the lesson goes on, uncomment one section's printing lines at a time and run the file again. In VS Code, select only the commented lines of that section and press `Command+/` (`Ctrl+/` on Windows). A selection that includes an uncommented line comments every line instead, so leave the uncommented lines out of the selection. The explanations and expected output are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. One line ends in an error on purpose, and it ends with `# crashes on purpose`. To see the error, uncomment that line, run the file, and then comment the line out again.

## Challenge: Keep the Return Value

The challenge section of `02_wrapping_a_function.py` wraps a function that returns a value, and its last line prints `None`. Change `wrapper` in `announce()` at the top of the file so that the last line prints `HI, MAYA!`. The `greet()` examples above it print the same lines before and after your change.

## Challenge: `@requires_reserved`

`03_a_decorator_that_refuses.py` has a `requires_reserved` decorator near the top that returns the method unchanged, so the file runs before you start. Finish the decorator so that it refuses a call unless the reservation is reserved. Then put `@requires_reserved` above `pay()` and delete the guard clause inside `pay()`, so that `pay()` contains only the line that changes the status. The challenge section's lines print the same output before and after your change, because the hand-written guard clause refuses the second payment until you replace it with the decorator.

## Testing a Status Guard

`guard-practice/` is a small project set up the way every Mod 2 repository is: the two decorators and `Reservation` in `src/reservation.py`, the tests in `tests/test_reservation.py`, and a `pytest.ini` that tells pytest where to find both. Run the tests from inside the folder, with your virtual environment turned on and pytest installed:

```sh
cd guard-practice
pytest
```

Both tests pass. Then, for the lesson's "Predict, then run", delete the `@requires_paid` line above `check_in()` in `src/reservation.py`, and run `pytest` again. Only `test_checking_in_before_paying_is_refused` fails, with `AssertionError: assert 'checked_in' == 'reserved'`. Put the line back afterwards.
