# Assignment 10 - Task 2

items = ["Vadim", 25, 1.80, True, "MIBA", 2026, "Python"]

string_count = 0

for item in items:
    if isinstance(item, str):
        string_count += 1

print("List:", items)
print("Number of strings:", string_count)
