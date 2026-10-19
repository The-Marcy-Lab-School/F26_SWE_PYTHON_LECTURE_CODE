# The first index picks the "row" and the second index picks the "column".

coordinates = [
    [30, 90],
    [40, 74],
    [34, 118],
    [42, 88],
    [39, 77],
]

new_orleans = coordinates[0]
new_orleans_lat = coordinates[0][0]
new_orleans_long = coordinates[0][1]

print(new_orleans)
print(new_orleans_lat)
print(new_orleans_long)

print(len(coordinates))     # 5, the number of rows
print(len(coordinates[0]))  # 2, the number of columns in the first row
