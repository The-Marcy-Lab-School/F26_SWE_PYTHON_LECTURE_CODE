# my_name is global. Reachable anywhere in this file.
my_name = 'Jayson'

def greet():
    # `my_name` is reachable anywhere within this file, even in lower scopes like in this function
    print(f"Hi, my name is {my_name}")

greet()

def greet_friend(friend):
    # Parameters like `friend` are local. Reachable anywhere in this function.

    if friend == "":
        # message is local to greet_friend. It can't be accessed outside of the function
        message = "I can't say hi if I don't know your name!"
    else:
        # This is the same variable as the one above, assigned a different value.
        message = f"Hi, {friend}, I'm {my_name}. Nice to meet you."

    # message is still reachable here, after the if/else is finished.
    print(message)

greet_friend("")
greet_friend('Jane')

# Predict, then run: What happens when you uncomment the line below?
# print(message, my_name)
