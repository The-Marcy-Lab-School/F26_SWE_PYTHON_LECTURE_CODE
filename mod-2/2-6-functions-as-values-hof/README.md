# 2.6 Functions as Values: Callbacks, Higher-Order Functions, and Closures

Every file in this folder follows one part of the lesson, and all of them use the lesson's `Event` and `Venue` classes and its four events at Riverside Community Hall. Run any file with `python3`, for example:

```sh
python3 01_two_searches.py
```

The lesson's case study check uses the case study repository, `swe-casestudy-2-venue-tickets`. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_two_searches.py` | Two Searches, Written Twice |
| `02_functions_are_values.py` | Functions Are Values |
| `03_passing_a_function.py` | Passing a Function to a Function, and Challenge: Finding Attendees |
| `04_the_function_not_its_result.py` | Passing the Function, Not Its Result |
| `05_lambda.py` | Writing a Function Inline with `lambda` |
| `06_sorting_with_key.py` | Sorting and Choosing with `key=`, and Challenge: The Event Listings |
| `07_functions_that_return_functions.py` | Functions That Return Functions, and Closures |
| `08_advanced_topics.py` | Advanced Topics |

Each numbered file runs as it is. Below the first part, the file is divided into sections named after the lesson's headings. In each section, the definitions and other lines that print nothing are already uncommented, so they run without changing the file's output. The lines that print are commented out. As the lesson goes on, uncomment one section's printing lines at a time and run the file again. In VS Code, select only the commented lines of that section and press `Command+/` (`Ctrl+/` on Windows). A selection that includes an uncommented line comments every line instead, so leave the uncommented lines out of the selection. The explanations and expected output are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. A few lines end in an error on purpose, and they end with `# crashes on purpose`. Those lines stay commented when you uncomment their section, so the rest of the file still runs. To see the error, uncomment that one line, run the file, and then comment the line out again.

## Challenge: Finding Attendees

The challenge section of `03_passing_a_function.py` gives `Venue` an `add_attendee()` method and a `find_attendees()` method that return `None`, and two named functions that also return `None`. The section runs before you start, and its two printing lines are commented out. Uncommented before you finish, they print `None` twice. Once you finish all four, they print the two lists shown in its comments.

## Challenge: The Event Listings

The challenge section of `06_sorting_with_key.py` has one function for each of the three listings, and each returns `None` until you finish it. Each function needs a single call to `sorted()`, `min()`, or `max()` with a `key`.
