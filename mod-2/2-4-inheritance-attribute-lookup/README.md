# 2.4 Inheritance and Attribute Lookup

Every file in this folder follows one part of the lesson, and most of them use the lesson's `Event`, `Concert`, `Workshop`, and `Screening` classes. Run any file with `python3`, for example:

```sh
python3 01_three_kinds_of_event.py
```

The lesson's case study checks use the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_three_kinds_of_event.py` | Three Kinds of Event |
| `02_defining_a_subclass.py` | Defining a Subclass, Adding to a Subclass with `super().__init__()`, Overriding a Method, and Extending a Method with `super()` |
| `03_workshop.py` | Challenge: A Workshop |
| `04_class_attributes.py` | Class Attributes, and Attribute Lookup |
| `05_inheritance_or_composition.py` | Inheritance or Composition? |
| `06_advanced_topics.py` | Advanced Topics |
| `inheritance-practice/` | Testing Each Kind of Event |

Each numbered file runs as it is. Below the first part, the file is divided into sections named after the lesson's headings. In each section, the definitions and other lines that print nothing are already uncommented, so they run without changing the file's output. The lines that print are commented out. As the lesson goes on, uncomment one section's printing lines at a time and run the file again. In VS Code, select only the commented lines of that section and press `Command+/` (`Ctrl+/` on Windows). A selection that includes an uncommented line comments every line instead, so leave the uncommented lines out of the selection. The explanations and expected output are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. A few sections end in an error on purpose, and their comment says so: comment those lines out again before you go on, so the rest of the file still runs. Lines that end with `# crashes on purpose` work the same way.

`01_three_kinds_of_event.py` and `05_inheritance_or_composition.py` have no commented sections. Each one runs as a whole.

## Challenge: A Workshop

`03_workshop.py` holds the lesson's `Event` class and an empty `Workshop` subclass. Until `Workshop` has its own `__init__` that takes `materials_fee`, the line that creates `pottery` stops the file with `TypeError: Event.__init__() got an unexpected keyword argument 'materials_fee'`, because the `__init__` that `Workshop` receives from `Event` has no `materials_fee` parameter. Each `print()` below it says what it should print once the challenge is done.

## Testing Each Kind of Event

`inheritance-practice/` is a small project set up the way every Mod 2 repository is: `Event` and its three kinds in `src/events.py`, the tests in `tests/test_events.py`, and a `pytest.ini` that tells pytest where to find both. Run the tests from inside the folder, with your virtual environment turned on and pytest installed:

```sh
cd inheritance-practice
pytest
```

All three tests pass. Then, for the lesson's "Predict, then run", change the last line of `Workshop.ticket_price()` in `src/events.py` from `return super().ticket_price() + self.materials_fee` to `return self.materials_fee`, and run `pytest` again. Only the workshop test fails. Change the line back afterwards.
