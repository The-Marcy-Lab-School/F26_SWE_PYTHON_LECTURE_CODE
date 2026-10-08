# Predict, then run: What does this print?
# Why doesn't the last return statement need an if statement?

def is_it_hot(temp):
    if temp > 100:
        return "So Hot!"
    if temp > 90:
        return "Yes!"
    if temp > 75:
        return "Eh"
    return "Nah"

print(is_it_hot(105))
# Output: ???
