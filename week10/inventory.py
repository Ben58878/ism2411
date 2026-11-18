# Reflection 1:
# The most surprising thing about Python lists is that they can be changed
# after they are created. I also learned that lists can store multiple items
# and make it easier to organize information.

# Reflection 2:
# At a business job, a list could help keep track of daily sales.
# Instead of manually calculating totals in Excel, Python could automatically
# calculate totals, averages, and identify the highest and lowest sales.
# EXERCISE 1: Build the list

inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))

# EXERCISE 2: Index practice

print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# EXERCISE 3: Slicing

print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# EXERCISE 4: Modify

inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# EXERCISE 5: Tuple comparison

coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because they cannot be changed accidentally.")

print(coords)

# EXERCISE 6: Average of a list of sales

sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# EXERCISE 7: Accumulator pattern

prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original prices:", prices)
print("Discounted prices:", discounted)

# EXERCISE 8: Filter above threshold

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Average:", round(sum(high_sales) / len(high_sales), 2))
