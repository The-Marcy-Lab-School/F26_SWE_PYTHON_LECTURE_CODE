# Challenge: Predict what each expression will produce. Then check your prediction in the Python REPL.
#
# Don't run this file. Python evaluates each expression and throws the value away without showing it.
# Use the REPL instead, which shows you the value of each expression you type:
#   1. In the Terminal, run python3 with no file name after it. The prompt changes to >>>
#   2. Copy one expression from this file, paste it after the >>> prompt, and press Enter.
#   3. The REPL prints the value. Compare it to your prediction, then move on to the next expression.
#   4. When you are done, type exit() and press Enter to return to the Terminal.

# What you would expect to happen usually happens
10 + 5 * 2
False and True
not False
not not False
not False and True
not (False and True)
"ana" in "banana"
None is None

# Slightly unexpected results
"10" > "2"
"a" > "B"
8 / 2
"3" * 5
"5" + 5
not 0
not 1
not 2
True + True + False
[1, 2] * 2

# Huh?
0 or "Python"
0.1 + 0.2 == 0.3
[1, 2] == [1, 2]
[1, 2] is [1, 2]
