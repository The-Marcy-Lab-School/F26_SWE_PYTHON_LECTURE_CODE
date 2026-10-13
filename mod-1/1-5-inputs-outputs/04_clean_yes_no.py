# Run this file a few times. Type yes, then YES, then " Yes" with a space in front.
# Then remove .strip().lower() from the first line and try the same answers again.

answer = input("Do you want to continue? (yes/no) ").strip().lower()

if answer == "yes":
    print("Let's keep going!")
else:
    print("Okay, see you later.")
