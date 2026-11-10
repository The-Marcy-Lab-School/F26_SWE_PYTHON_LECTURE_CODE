# 2.1 Intro to OOP: Classes, `__init__`, and `self`

Every file in this folder follows one part of the lesson, and most of them use the lesson's `Event` class for the venue's events. Run any file with `python3`, for example:

```sh
python3 01_data_types_and_classes.py
```

The lesson's case study checks use the case study repository, `swe-casestudy-2-venue-tickets`, which you clone at the start of the lesson. Nothing in this folder depends on it.

## The Files

| File | Lesson section |
| --- | --- |
| `01_data_types_and_classes.py` | What is a Data Type? And What is a Class?: Every Value is an "Instance" of a "Class", `dir` Tells Us what a Class and its Instances Can Do, and Instances Find Their Methods in Their Class |
| `02_classes_and_instances.py` | Creating your own Classes: Defining a Class, Attributes, `__init__` Gives Every Instance the Same Shape, and A Common Mistake: Data Goes on `self` |
| `03_methods_and_self.py` | Methods and `self`: Writing a Method, `self` Is the Value Before the Dot, and A Method That Takes Arguments |
| `04_room_rentals.py` | Challenge: Room Rentals |
| `05_encapsulation_and_the_interface.py` | Encapsulation and the Interface: Parallel Lists Drift Apart, Dictionaries Keep the Data Together but Not the Rules, One Place for the Data and Its Rules, The Interface, and Dictionary or Class? |
| `06_advanced_topics.py` | Advanced Topics |

Each file starts with code that runs as it is. Below it, the rest of the file is commented out in sections named after the lesson's headings. As the lesson goes on, uncomment one section at a time and run the file again. In VS Code, select the whole section, from its `# # ----------` heading to its last line, and press `Command+/` (`Ctrl+/` on Windows). The headings and explanations are commented twice, so they stay comments while the code becomes runnable.

Some sections ask you to predict the output before you run them, so read the comment at the top of each section first. Several lines end with `# crashes on purpose`. Uncomment one to see the error, then comment it out again so the rest of the file still runs.

## Challenge: Room Rentals

`04_room_rentals.py` holds a `Room` class with its method names written for you. Each method starts out doing nothing or returning `None`, so the file runs and prints `None` until you finish it. The comment at the top says what each method should do, and the comments beside the `print()` calls say what each one should print when you are done.
