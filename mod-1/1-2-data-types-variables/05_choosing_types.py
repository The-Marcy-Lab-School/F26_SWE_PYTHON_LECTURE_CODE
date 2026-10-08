# We use numbers when we want to use arithmetic operators
celsius = 100.0
fahrenheit = celsius * 9/5 + 32
print(f"{celsius}°C is {fahrenheit}°F")

# We use booleans when we want to use logical operators
is_on = True
has_power = False
generator_is_running = True

there_is_light = is_on and (has_power or generator_is_running)
print(f"The lights are on: {there_is_light}")

# We use strings when we want to do things like use the membership operator
email = "ben@marcylabschool.org"
print(f"{email} is a Marcy email: {"@marcylabschool.org" in email}")
