# This program prints nothing. Is it doing anything?
# Run it with: time python3 05_no_output.py

x = 0

# A loop with 100 million iterations will take a few seconds to run! Increase that number to a billion and it could take a minute or more.
for i in range(100_000_000):
    x += 1
