# Lists share these tools with strings: indexes, len(), slicing, in, and for loops.

items = ['coffee', 'bagel', 'juice', 'muffin']
print(f"type() on a list returns {type(items)}")

print(f"I bought {len(items)} items")
print(f"My first item was {items[0]}")
print(f"My last item was {items[-1]}")
print(f"My first two items were {items[0:2]}")
print(f"Did I buy a bagel? {'bagel' in items}")
print('Here is everything I bought:')

for item in items:
    # item holds the "current" item that we're looking at in this iteration of the loop
    print(item)
