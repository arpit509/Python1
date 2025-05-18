# n = int(input("Enter number of elements: "))
# list1 = []

# # Taking input
# for i in range(n):
#     element = int(input("Enter element: "))
#     list1.append(element)
# print(list1)
# max1 = list1[0]
# secondmax = list1[0]

# for i in range(n):
#     if list1[i] > max1:
#         secondmax = max1
#         max1 = list1[i]
#     elif list1[i] > secondmax and list1[i] != max1:
#         secondmax = list1[i]
# print("Second highest number is : ", secondmax)


"""Assignment 2 """

# n = int(input("Enter number of elements: "))
# list1 = []
# odd_li = []
# even_li = []

# # Taking input
# for i in range(n):
#     element = int(input("Enter element: "))
#     list1.append(element)
# print(list1)

# for i in range(n):
#     if list1[i] % 2 == 0:
#         even_li.append(list1[i])
#     else:
#         odd_li.append(list1[i])
# print("Even numbers: ", even_li)
# print("Odd numbers: ", odd_li)


"""Assignment 3"""

n = int(input("Enter number of elements: "))
list1 = []

# Taking input
for i in range(n):
    element = int(input("Enter element: "))
    list1.append(element)
print(list1)

total = int(input("Enter the total: "))
pair = []
for i in range (n):
    
    for j in range(i, n):
        if list1[i] + list1[j] == total:
            pair.append(list1[i])
            pair.append(list1[j])
print("Sum Pair : ", pair)

