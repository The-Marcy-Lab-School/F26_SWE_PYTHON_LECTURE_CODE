# 1.10 Test-Driven Development

This lesson has no prepared code files. Instead, you build a small project called `testing-practice` from scratch, one file at a time, as the lesson goes on. The Comprehensions lesson reuses the same project, so keep it when you are done.

Create `testing-practice` inside this folder. This repository's `.gitignore` already lists `.venv/` and `__pycache__/`, so the environment you create will not show up in `git status`.

## Setup

Run these commands in the Terminal, one step at a time, from inside the `1-10-test-driven-development` folder.

1. Create the project folder and move into it.

   ```sh
   mkdir testing-practice
   cd testing-practice
   ```

2. Create a virtual environment and activate it. Check that your prompt starts with `(.venv)`.

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install `pytest` and record what is installed.

   ```sh
   pip install pytest
   pip freeze > requirements.txt
   ```

4. Create one folder for source code and one for tests.

   ```sh
   mkdir src tests
   ```

5. Create `src/calc.py` with the `add` function from the lesson, and `tests/test_calc.py` with its first test.

   ```python
   # src/calc.py
   def add(a, b):
       return a + b
   ```

   ```python
   # tests/test_calc.py
   from src.calc import add


   def test_add():
       """add - adds two positive numbers"""
       assert add(1, 2) == 3
       assert add(10, 5) == 15
   ```

6. Run the tests. pytest prints a `.` for the one test that passed, and the last line says `1 passed`.

   ```sh
   python3 -m pytest
   ```

The project should now look like this:

```
testing-practice/
├── .venv/
├── requirements.txt
├── src/
│   └── calc.py
└── tests/
    └── test_calc.py
```

Always run `python3 -m pytest` from inside `testing-practice`, the folder that contains `src/`. Run from anywhere else and the import on the first line of every test file fails with `ModuleNotFoundError: No module named 'src'`. The lesson explains why in the hint under First Test.

## Files You Create During the Lesson

Each section of the lesson adds to the project. Copy the code from the lesson into the files below as you reach each section, then run the tests.

| File                                                            | Lesson section                                                        |
| --------------------------------------------------------------- | --------------------------------------------------------------------- |
| `src/calc.py`, `tests/test_calc.py`                             | First Test, through Checking `True`, `False`, and Decimals            |
| `src/double_all.py`, `tests/test_double_all.py`                 | Refactoring with Tests, and all four steps of Test-Driven Development |
| `src/bank.py`, `tests/test_bank.py`                             | Testing Errors                                                        |
| `src/bank.py` (below `withdraw`), `tests/test_bank_accounts.py` | Challenge: Bank Accounts                                              |

Two sections ask you to break something on purpose, read what pytest reports, and then put it back:

- **Reading a Failure:** change the expected value in `test_add_negatives` from `-5` to `-6`.
- **Testing That a Function Raises:** delete the whole `if` statement from `withdraw`, so that it allows the overdraft.

To run a single test file instead of all of them, give pytest its path. To see every test by name, add `-v`.

```sh
python3 -m pytest tests/test_double_all.py
python3 -m pytest -v
```

When you are finished with the lesson, the project looks like this:

```
testing-practice/
├── .venv/
├── requirements.txt
├── src/
│   ├── calc.py
│   ├── double_all.py
│   └── bank.py
└── tests/
    ├── test_calc.py
    ├── test_double_all.py
    ├── test_bank.py
    └── test_bank_accounts.py
```
