print(bool(0))         # -> False
print(bool(""))        # -> False
print(bool(None))      # -> False
print(bool([]))        # -> False (an empty list)
print(bool(100))       # -> True
print(bool("hello"))   # -> True

# Because an if calls bool() for you, `if not friend:` does the same job as `if friend == "":`
def greet_friend(friend):
    if not friend:
        return "I can't say hi if I don't know your name!"
    return f"Hi, {friend}! Nice to meet you."

print(greet_friend(""))      # Output: I can't say hi if I don't know your name!
print(greet_friend("Jane"))  # Output: Hi, Jane! Nice to meet you.
