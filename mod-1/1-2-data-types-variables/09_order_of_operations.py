# This code is meant to convert 212°F to 100°C.
# Walk through both versions one operator at a time. At which operation do they differ?

fahrenheit = 212
celsius = fahrenheit - 32 * 5 / 9
print(celsius)

celsius = (fahrenheit - 32) * 5 / 9
print(celsius)

# What is the order of operations? What is the value stored in report?
temperature = 85
report = "hot" if temperature - 10 > 70 else "mild"
print(report)
