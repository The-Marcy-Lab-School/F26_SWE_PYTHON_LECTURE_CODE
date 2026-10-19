# The id() function returns a number that identifies where a value lives.
#
# items ──► [ slot 0 | slot 1 | slot 2 ]
#               │        │        │
#               ▼        ▼        ▼
#           'coffee'  'bagel'  'juice'

nums = [1, 2, 3]
clone = nums

print(id(nums))          # some large number, like 4395782592
print(id(clone))         # the exact same number
print(nums is clone)     # True: `is` asks whether two variables reference the same object
