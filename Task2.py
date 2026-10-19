# Assignment 10 - Task 2

items = ["Vadim", 25, 1.80, True, "MIBA", 2026, "Python"]

cnt = 0

for i in items:
    if type(i) is str:
        cnt += 1

print("List:", items)
print("Number of strings:", cnt)
