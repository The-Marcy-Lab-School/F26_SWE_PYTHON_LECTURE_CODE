# Challenge: Refactor with Tests 🏗️🏗️🏗️🏗️🏗️
# Run the tests first and watch all three pass:  python3 -m pytest
# Then refactor double_all_purely to use a list comprehension and run the tests again.
# If every test still passes, the comprehension does what the loop did.

def double_all_purely(items):
    doubled = []
    for value in items:
        doubled.append(double(value))
    return doubled


def double(value):
    if isinstance(value, (int, float, str)):
        return value * 2
    else:
        return value
