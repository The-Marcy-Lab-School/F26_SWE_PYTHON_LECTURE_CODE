# 2.3 Properties: Non-Public Attributes and `@property`

Every file in this folder follows one part of the lesson, and most of them use the lesson's `Event` class. Run any file with `python3`, for example:

```sh
python3 01_going_around_the_rules.py
```

The lesson's case study checks use the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_going_around_the_rules.py` | Going Around the Rules |
| `02_properties.py` | Non-Public Attributes and `@property`: Step 1. A Value Other Code Can Read but Not Assign, and Step 2. Refusing a Wrong Value with a Setter |
| `03_base_price.py` | Challenge: Base Price |
| `04_the_underscore_is_a_convention.py` | The Underscore Is a Convention |
| `05_advanced_topics.py` | Advanced Topics |
| `refusal-practice/` | Testing a Refusal, and Challenge: Test the Base Price |

Each numbered file starts with code that runs as it is. Below it, the rest of the file is commented out in sections named after the lesson's headings. As the lesson goes on, uncomment one section at a time and run the file again. In VS Code, select the whole section, from its `# # ----------` heading to its last line, and press `Command+/` (`Ctrl+/` on Windows). The headings and explanations are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. A few of those sections end in an error on purpose, and their comment says so: comment the section out again before you go on, so the rest of the file still runs. Lines that end with `# crashes on purpose` work the same way.

## Challenge: Base Price

`03_base_price.py` holds an `Event` class whose `base_price` is still a plain attribute. The file runs before you start, and its last line prints `-15`, because nothing refuses a negative price yet. Once your setter works, the line that assigns `-15` raises a `ValueError` instead, and the last `print()` never runs.

## Testing a Refusal

`refusal-practice/` is a small project set up the way every Mod 2 repository is: the `Event` class in `src/event.py`, the tests in `tests/test_event.py`, and a `pytest.ini` that tells pytest where to find both. Run the tests from inside the folder, with your virtual environment turned on and pytest installed:

```sh
cd refusal-practice
pytest
```

Both tests pass. Then:

1. For the lesson's "Predict, then run", swap the two lines in the `capacity` setter in `src/event.py`, so that it stores the value before it checks it, and run `pytest` again. Swap the lines back afterwards.
2. For Challenge: Test the Base Price, copy your `base_price` property from `03_base_price.py` into `src/event.py`, and add three tests to `tests/test_event.py`: a negative price is refused, a refused price leaves the stored price unchanged, and a price of `0` is accepted.
