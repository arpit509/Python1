# Taking input for first set
n1 = int(input("Enter number of elements in first set: "))
set1 = set()
for _ in range(n1):
    element = int(input("Enter element: "))
    set1.add(element)

# Taking input for second set
n2 = int(input("Enter number of elements in second set: "))
set2 = set()
for _ in range(n2):
    element = int(input("Enter element: "))
    set2.add(element)

# Performing operations
print("Set 1:", set1)
print("Set 2:", set2)

print("Union:", set1 | set2)  # Union of sets
print("Intersection:", set1 & set2)  # Intersection of sets
print("Difference (Set1 - Set2):", set1 - set2)  # Difference (elements in Set1 but not in Set2)
print("Difference (Set2 - Set1):", set2 - set1)  # Difference (elements in Set2 but not in Set1)
print("Symmetric Difference:", set1 ^ set2)  # Symmetric Difference (elements in either set but not both)
