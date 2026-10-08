# Predict, then run: What if we replace all of the elif and else statements with other if statements?

def is_it_hot(temp):
    if temp > 75:
        print("Eh")
    if temp > 90:
        print("Yes!")
    if temp > 100:
        print("So Hot!")
    if temp <= 75:
        print("Nah")

is_it_hot(105)
# Output: ???
