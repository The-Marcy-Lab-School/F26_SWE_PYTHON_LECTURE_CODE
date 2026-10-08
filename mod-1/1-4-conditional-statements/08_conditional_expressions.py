# Okay - Use an if statement to choose which code block to execute
def is_this_even(num):
    if num % 2 == 0:
        message = 'it is even!'
    else:
        message = 'it is odd!'
    print(message)

is_this_even(4)
is_this_even(5)

# Better - Use a conditional expression to choose which value to assign to message
def is_this_even(num):
    message = "it is even!" if num % 2 == 0 else "it is odd!"
    print(message)

is_this_even(4)
is_this_even(5)
