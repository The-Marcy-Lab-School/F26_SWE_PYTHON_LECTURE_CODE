# Predict: Which of these calls work, and what do they print? Which one crashes, and why?

def make_greeting(name, punctuation="!"):
    return f"Hello, {name}{punctuation}"

print(make_greeting("Ada"))
print(make_greeting("Ada", "?"))
print(make_greeting(punctuation="...", name="Ada"))
print(make_greeting())
