class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def fractional_knapsack(capacity, items):
    # Sort items by value to weight ratio in decreasing order
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0.0  # Variable to store the maximum value

    # Loop through the sorted items
    for item in items:
        if capacity >= item.weight:
            # If the item can fit into the knapsack, take the whole item
            capacity -= item.weight
            total_value += item.value
        else:
            # If the item can't fit completely, take the fraction of the item
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break  # Knapsack is full after this

    return total_value

items = []
n = int(input("Enter number of items : "))
for i in range(n):
  value = int(input("Enter value of : "))
  weight = int(input("Enter weight of : "))
  item = Item(value, weight)
  items.append(item)
capacity = int(input("Enter capacity of bag : "))

max_value = fractional_knapsack(capacity, items)
print(f"Maximum value in knapsack = {max_value}")
