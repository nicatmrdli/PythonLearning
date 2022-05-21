# In a 2D list, you can access a number with coordinates.
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[2][1]);
# Here a user can access a number with the row and column
# In Python, the digits starts at 0, so to access 8, we need to coordinate with 0 in mind.

number_grid1 = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

for row in number_grid1:
    for col in row:
        # This will give us each element in the number grid.
        print(col)