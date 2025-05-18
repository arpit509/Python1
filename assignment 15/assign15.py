from functools import reduce

# Given data
prices_usd = [50, 120, 250, 75, 40, 600, 850, 30, 95, 410]

# 1. Convert Prices: USD to INR (1 USD = 83 INR)
prices_inr = list(map(lambda price: price * 83, prices_usd))
print("Converted Prices (INR):\n", prices_inr)


# 2. Filter: Only products priced at ₹5000 or less
affordable_prices = list(filter(lambda price: price <= 5000, prices_inr))
print("\nFiltered Prices (≤ ₹5000):")
print(affordable_prices)

# 3. Reduce: Total cost of remaining products
total_cost = reduce(lambda x, y: x + y, affordable_prices)
print("\nTotal Cost of Remaining Products:")
print(total_cost)
