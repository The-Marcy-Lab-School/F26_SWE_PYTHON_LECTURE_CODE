# Predict, then run: What happens if we rearrange the conditional statements like so?

def is_it_hot(temp):
    if temp > 75:
        print("Eh")
    elif temp > 90:
        print("Yes!")
    elif temp > 100:
        print("So Hot!")
    else:
        print("Nah")

is_it_hot(80)
# Output: ???

is_it_hot(95)
# Output: ???

is_it_hot(105)
# Output: ???

is_it_hot(60)
# Output: ???
