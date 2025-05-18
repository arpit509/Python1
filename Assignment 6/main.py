"""Assignment 1 """

# n = int(input("Enter no of elements: "))
# list1 = []
# avg1 = 0 
# sum1 = 0
# for i in range(0, n):
#     element = int(input("Enter element: "))
#     list1.append(element)
# print(list1)
# min1 = list1[0]
# max1 = list1[0]
# for i in range(len(list1)): 
#     if list1[i] > max1:
#         max1 = list1[i]
#     if list1[i] < min1:
#         min1 = list1[i]
#     sum1 = sum1 + list1[i]
#     avg1 = sum1/n
# print("Max element is: ", max1)
# print("Min element is: ", min1)
# print("Sum of elements is: ", sum1)
# print("Average of elements is: ", avg1)


"""Assignment 2"""
# n = int(input("Enter no of elements: "))
# list1 = []


# for i in range(n):
#     element = int(input("Enter element: "))
#     list1.append(element)

# # Reversing the list manually
# reversed_list = []
# for i in range(n - 1, -1, -1):  # Loop from last index to first
#     reversed_list.append(list1[i])

# # Output the reversed list
# print("Reversed list:", reversed_list)


"""Assignment 3 """

# n = int(input("Enter no of elements: "))
# list1 = []

# for i in range(n):
#     element = int(input("Enter element: "))
#     list1.append(element)

# search = int(input("Enter element to search: "))
# if search in list1:
#     print("Element found")
# else:
#     print(-1)


"""Assignnemnt 4"""

# n = int(input("Enter number of elements: "))
# list1 = []

# # Taking input
# for i in range(n):
#     element = int(input("Enter element: "))
#     list1.append(element)
# print(list1)
# # Removing duplicates manually
# check_list = []
# for item in list1:
#     if item not in check_list:  # Check if item is already in unique_list
#         check_list.append(item)

# # Output the list without duplicates
# print("List after removing duplicates:", check_list)


"""Assignmrnt 5"""

n = int(input("Enter number of elements: "))
list1 = []
list2= []

# Taking input
for i in range(n):
    element = int(input("Enter element(1st list): "))
    list1.append(element)
print(list1)

for i in range(n):
    element = int(input("Enter element (2nd List): "))
    list2.append(element)
print(list2)

merge_list = list1 + list2
# for i in range (n):
#     merge_list.append(list1[i])
# for i in range (n):
#     merge_list.append(list2[i])
print("Merged List : ", merge_list)

