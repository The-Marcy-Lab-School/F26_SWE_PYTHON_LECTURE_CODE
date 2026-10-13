# Predict, then run: Many receipts hide every digit of the card number except the last four.
# What does this print? How many stars would a 15-digit card number get?

card = "4111222233334444"
print("*" * (len(card) - 4) + card[-4:])
