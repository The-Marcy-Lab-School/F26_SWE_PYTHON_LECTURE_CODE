# 1.11 Comprehensions and Common List Operations

Every file in this folder uses the café's list of purchases from the lesson. Run any file with `python3`, for example:

```sh
python3 01_cafe.py
```

## The Café Report

`01_cafe.py` is where you complete every café report challenge, along with Challenge: Coffee Revenue. Each challenge has its own helper function, which starts out returning a placeholder value such as `[]` or `None`. The comment above each function says what the finished function should print or return.

`generate_report()` at the bottom of the file calls every helper and prints the café's end-of-day report. The file runs before any challenge is done, so run it after each challenge to watch that challenge's line of the report fill in.

## The Lesson's Examples

The other files hold the lesson's examples, one file per job:

| File | Lesson section |
| --- | --- |
| `02_for_loop.py` | 1. Do something with every value without producing a result |
| `03_transform.py` | 2. Transforming with List Comprehensions, through Imperative vs. Declarative Code |
| `refactor-with-tests/` | Challenge: Refactor with Tests (see the steps below) |
| `04_filter.py` | 3. Filtering with an `if` |
| `05_reduce.py` | 4. Reduce a List of Values Into One Value, through Generating a Frequency Counter |
| `06_find_first.py` | 5. Finding the First Match |
| `07_sorting.py` | 6. Sorting with `sorted()` and `.sort()` |
| `08_combining_steps.py` | Combining Steps |
| `09_advanced_topics.py` | Advanced Topics |

Each of these files starts with code that runs as it is. Below it, the rest of the file is commented out in sections named after the lesson's headings. As the lesson goes on, uncomment one section at a time and run the file again. In VS Code, select the whole section, from its `# # ----------` heading to its last line, and press `Command+/` (`Ctrl+/` on Windows). The headings and explanations are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. One section in `05_reduce.py` ends with a line that crashes on purpose. Uncomment it to see the error, then comment it out again so the rest of the file still runs.

## Challenge: Refactor with Tests

`refactor-with-tests/double_all.py` holds `double_all_purely`, written as a loop, and `refactor-with-tests/test_double_all.py` holds three tests for it. Run these commands in the Terminal, one step at a time.

1. Move into the folder, then create a virtual environment and activate it. Check that your prompt starts with `(.venv)`.

    ```sh
    cd refactor-with-tests
    python3 -m venv .venv
    source .venv/bin/activate
    ```

2. Install `pytest`.

    ```sh
    pip install pytest
    ```

3. Run the tests before you change anything. pytest prints a `.` for each test that passed, and the last line says `3 passed`.

    ```sh
    python3 -m pytest
    ```

4. Refactor `double_all_purely` in `double_all.py` to use a list comprehension, then run `python3 -m pytest` again. If all three tests still pass, the comprehension does what the loop did.
