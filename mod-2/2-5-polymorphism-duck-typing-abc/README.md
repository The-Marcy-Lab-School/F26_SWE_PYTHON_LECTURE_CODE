# 2.5 Polymorphism, Duck Typing, and Abstract Base Classes

Every file in this folder follows one part of the lesson, and most of them use the lesson's `Event`, `Concert`, `Workshop`, and `Screening` classes. Run any file with `python3`, for example:

```sh
python3 01_asking_which_kind_of_event.py
```

The lesson's case study checks use the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_asking_which_kind_of_event.py` | Asking Which Kind of Event |
| `02_letting_each_kind_decide.py` | Letting Each Kind of Event Decide |
| `03_library_loans.py` | Challenge: Library Loans Without `isinstance()` |
| `04_duck_typing.py` | Duck Typing |
| `05_abstract_base_classes.py` | Abstract Base Classes, and Abstract Base Class or Duck Typing? |
| `06_advanced_topics.py` | Advanced Topics |
| `abc-practice/` | Testing That an Incomplete Kind of Event Is Refused |

Each numbered file runs as it is. Below the first part, the file is divided into sections named after the lesson's headings. In each section, the definitions and other lines that print nothing are already uncommented, so they run without changing the file's output. The lines that print are commented out. As the lesson goes on, uncomment one section's printing lines at a time and run the file again. In VS Code, select only the commented lines of that section and press `Command+/` (`Ctrl+/` on Windows). A selection that includes an uncommented line comments every line instead, so leave the uncommented lines out of the selection. The explanations and expected output are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. A few sections end in an error on purpose, and their comment says so: comment those lines out again before you go on, so the rest of the file still runs. Lines that end with `# crashes on purpose` work the same way.

## Challenge: Library Loans Without `isinstance()`

`03_library_loans.py` holds the library's program as the lesson shows it, with the rules for loan periods and late fees in two functions that ask which kind of item they were given. The file runs before you start and prints three lines. After the refactor it should print the same three lines, and once `Audiobook('Born a Crime')` is on the shelf, a fourth: `Born a Crime: 14-day loan, $4 if 4 days late`.

## Testing That an Incomplete Kind of Event Is Refused

`abc-practice/` is a small project set up the way every Mod 2 repository is: the abstract `Event` and a `Concert` in `src/events.py`, the tests in `tests/test_events.py`, and a `pytest.ini` that tells pytest where to find both. Run the tests from inside the folder, with your virtual environment turned on and pytest installed:

```sh
cd abc-practice
pytest
```

All three tests pass. Then, for the lesson's "Predict, then run", delete the `@abstractmethod` line above `can_refund()` in `src/events.py`, and run `pytest` again. Only the `Festival` test fails, with `DID NOT RAISE TypeError`. Put the line back afterwards.
