# 1.9 Modules, Virtual Environments, and pytest

Every file in this folder works on the same café ordering program from the lesson. Run any file with `python3`, for example:

```sh
python3 01_one_long_block.py
```

The files follow the lesson in order:

| File | Lesson section |
| --- | --- |
| `01_one_long_block.py` | One Long Block of Code |
| `02_helper_functions.py` | Helper Functions and a `main()` Function |
| `cafe/orders.py`, `cafe/interface.py`, `cafe/main.py` | Modules, through A Traceback Across Two Files |
| `madlib-challenge/main.py` | Challenge: Split the Madlib |
| `03_standard_library.py` | The Standard Library |
| `cafe/test_orders.py` | Virtual Environments with `venv`, through pytest: A Package You Already Use (see the steps below) |

`01_one_long_block.py`, `02_helper_functions.py`, `cafe/main.py`, and `madlib-challenge/main.py` ask for input, so they run as they are.

## The `cafe` Folder

`cafe` holds the program split into three modules. Python looks for `orders.py` and `interface.py` in the same folder as `main.py`, so move into the folder before you run it:

```sh
cd cafe
python3 main.py
```

The code in these files matches the lesson line for line, so the line numbers in your traceback match the one in the lesson. The comments for each lesson section sit below the last line of code in `orders.py` and `main.py`, and one comment in `interface.py` names the change for A Traceback Across Two Files. Undo each change when you are done with its section.

## Virtual Environments, `pip`, and pytest

These sections of the lesson are commands, not Python files. Run them in the Terminal from inside the `cafe` folder, one step at a time.

1. Create a virtual environment and activate it. Check that your prompt starts with `(.venv)`.

    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    which python3
    ```

2. Install `pytest`. Count how many packages `pip` installs, then find out why with `pip show`.

    ```sh
    pip install pytest
    pip list
    pip show pytest
    ```

3. Record what is installed, and open the file it writes.

    ```sh
    pip freeze > requirements.txt
    ```

4. Run `git status`. `requirements.txt` appears as a new file, but `.venv/` and `__pycache__/` do not, because this repository's `.gitignore` already lists them.

5. Run the test in `test_orders.py`. pytest prints a `.` for the test that passed.

    ```sh
    python3 -m pytest
    ```

6. **Predict, then run:** Turn the environment off, then run the tests again. What happens?

    ```sh
    deactivate
    python3 -m pytest
    ```

    Activate the environment again with `source .venv/bin/activate` before moving on.
