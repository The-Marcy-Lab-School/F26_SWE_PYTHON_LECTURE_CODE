# Predict, then run: What does the first print statement show? Why didn't strip() and lower() change answer?

answer = '  YES '
answer.strip()
answer.lower()
print(answer)
# Output: ???

# Method chaining calls lower() on the new string that strip() returns
cleaned = answer.strip().lower()
print(cleaned)
# Output: yes
