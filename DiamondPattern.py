rows = int(input("Enter number of rows: "))

# Upper half
for i in range(1, rows + 1):
    print(" " * (rows - i) + "⭐ " * i)

# Lower half
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "⭐ " * i)