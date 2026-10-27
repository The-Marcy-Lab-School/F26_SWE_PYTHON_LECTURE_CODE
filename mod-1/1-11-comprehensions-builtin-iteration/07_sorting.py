# Job 6: Compare values to put them in order.
# Uncomment one section at a time as the lesson goes on.

# sorted() returns a new list. The source list is untouched.
prices = [3.50, 2.25, 3.50, 4.00, 3.00]
ordered = sorted(prices)
print(ordered)  # [2.25, 3.0, 3.5, 3.5, 4.0]
print(prices)   # [3.5, 2.25, 3.5, 4.0, 3.0]


# # ---------- .sort() Sorts In Place ----------
# # .sort() changes the list itself and returns nothing.

# prices = [3.50, 2.25, 3.50, 4.00, 3.00]
# prices.sort()   # sorts prices "in place"
# print(prices)   # [2.25, 3.0, 3.5, 3.5, 4.0]


# # ---------- Predict, then run: What Does .sort() Return? 🤔🤔🤔🤔🤔 ----------

# prices = [3.50, 2.25, 3.50, 4.00, 3.00]
# result = prices.sort()
# print(result)


# # ---------- Descending Order with reverse=True ----------

# prices = [3.50, 2.25, 3.50, 4.00, 3.00]
# print(sorted(prices, reverse=True))   # [4.0, 3.5, 3.5, 3.0, 2.25]
