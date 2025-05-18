# # Creating a nested tuple
# nested_tuple = (
#     (1, 2, 3),
#     (4, 5, 6),
#     (7, 8, 9)
# )

# # Printing the whole nested tuple
# print("Nested Tuple:", nested_tuple)

# # Accessing specific elements
# print("First inner tuple:", nested_tuple[0])
# print("Second element of second tuple:", nested_tuple[1][1])  # Output: 5
# print("Last element of last tuple:", nested_tuple[2][-1])  # Output: 9

"""Assignment 2 and 3 """
# Creating a tuple of integers
# numbers = (10, 25, 3, 7, 18, 42, 5)

# # Finding maximum and minimum values
# max_value = max(numbers)
# min_value = min(numbers)

# # Calculating sum of all elements
# total_sum = sum(numbers)

# # Printing results
# print("Tuple:", numbers)
# print("Maximum value:", max_value)
# print("Minimum value:", min_value)
# print("Sum of all numbers:", total_sum)

"""Assignment 4 and 5 """
# Given list
my_list = [10, 20, 30, 40]

# Convert list to tuple
my_tuple = tuple(my_list)
print("Converted Tuple:", my_tuple)

# Convert tuple back to list
converted_list = list(my_tuple)
print("Converted List:", converted_list)

# Given tuple
numbers_tuple = (25, 10, 5, 40, 30)

# Sort the tuple (sorted() returns a list, so convert it back to tuple)
sorted_tuple = tuple(sorted(numbers_tuple))

# Printing results
print("Original Tuple:", numbers_tuple)
print("Sorted Tuple:", sorted_tuple)
