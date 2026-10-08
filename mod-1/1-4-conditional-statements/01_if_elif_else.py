def is_it_hot(temp):
    if temp > 100:
        print("So Hot!")
    elif temp > 90:
        print("Yes!")
    elif temp > 75:
        print("Eh")
    else:
        print("Nah")

is_it_hot(80)
# Output: Eh

is_it_hot(95)
# Output: Yes!

is_it_hot(105)
# Output: So Hot!

is_it_hot(60)
# Output: Nah
