# import math

# int1 = 5
# float1 = 5.0
# string1 = "My name is "
# string2 = "Arpit"
# check = True

# print(int1)
# print(float1)
# print(string1)
# # print(string2)
# print(check)


# str1 = "My name is "
# str2 = "Arpit."
# str3 = str1 + str2
# print(str3)
# print(len(str1))
# print(str1[3:7])


# Integer to Float
# int_value = 10

# float_value = float(int_value)
# print("Changed Type : ", float_value)  # Output: 10.0

# # Float to Integer (truncates decimal part)
# float_value = 10.99
# int_value = int(float_value)
# print("Changed Type : ", int_value)  # Output: 10


# # String to Integer
# str_value = "25"
# int_value = int(str_value)
# print("Changed Type : ",int_value)  # Output: 25

# # String to Float
# str_value = "25.75"
# float_value = float(str_value)
# print("Changed Type : ",float_value)  # Output: 25.75



"""Assignment 3 """


# a = int(input("Enter first number(a) : "))
# b = int(input("Enter second number(b) : "))

# # Equala == a == b""to (==)
# print("a == b :",a == b)  # Output: False (10 is not equal to 20)

# # Not equal to (!=)
# print("a != b) :",  a!= b)  # Output: True (10 is not equal to 20)

# # Less than (<)
# print("a < b", a < b ) 
# # Greater than (>)
# print("a > b", a > b)  # Output: False (10 is not greater than 20)

# # Less than or equal to (<=)
# print("a <= b", a <= b)  # Output: True (10 is less than or equal to 20)

# # Greater than or equal to (>=)
# print("a>= b", a >= b)  # Output: False (10 is not greater than or equal to 20)

# a = int(input("Enter first number(a) : "))
# b = int(input("Enter second number(b) : "))

# # Using AND (Both conditions must be True)
# print("a > 5 and b > 15 : ",a > 5 and b > 15)   # Output: True (both conditions are True)
# print("a > 5 and b < 15: ",a > 5 and b < 15)   # Output: False (one condition is False)

# # Using OR (At least one condition must be True)
# print("a > 5 or b < 15 : ", a > 5 or b < 15)    # Output: True (one condition is True)

# # Using NOT
# print("not (a > b) : ", not (a > b))        # Output: True (a > b is False, so not makes it True)


# # Simple Assignment (=)
# x = int(input("Enter A number : "))
# print(x)  # Output: 10

# # Addition Assignment (+=)
# x += 5  # Equivalent to: x = x + 5
# print("x += 5 : ", x)  # Output: 15

# # Subtraction Assignment (-=)
# x -= 3  # Equivalent to: x = x - 3
# print("x -= 3 : ", x)  # Output: 12

# # Multiplication Assignment (*=)
# x *= 2  # Equivalent to: x = x * 2
# print("x *= 2 : ", x)  # Output: 24

# # Division Assignment (/=)
# x /= 4  # Equivalent to: x = x / 4
# print("x /= 4 : ", x)  # Output: 6.0 (division always returns float)

# # Floor Division Assignment (//=)
# x //= 2  # Equivalent to: x = x // 2
# print("x //= 2 : ", x)  # Output: 3 (integer division)

# # Modulus Assignment (%=)
# x %= 2  # Equivalent to: x = x % 2
# print("x %= 2 : ", x)  # Output: 1 (remainder when divided by 2)

# # Exponentiation Assignment (**=)
# x **= 3  # Equivalent to: x = x ** 3
# print("x **= 3 : ", x)  # Output: 1 (since 1^3 = 1)

# a = int(input("Enter first number(a) : "))
# b = int(input("Enter Second number(b) : "))

# # Bitwise AND (&) - Both bits must be 1
# print("a & b : ", a & b)  # Output: 1  (Binary: 0001)

# # Bitwise OR (|) - At least one bit must be 1
# print("a | b : ", a | b)  # Output: 7  (Binary: 0111)

# # Bitwise XOR (^) - Bits must be different
# print("a ^ b : ", a ^ b)  # Output: 6  (Binary: 0110)

# # Bitwise NOT (~) - Flips all bits (2's complement representation)
# print("~a : ", ~a)     # Output: -6 (Binary: 1010 in 2's complement)

# # Left Shift (<<) - Shifts bits to the left, adding zeros
# print("a << 1 : ", a << 1) # Output: 10 (Binary: 1010)

# # Right Shift (>>) - Shifts bits to the right, removing bits
# print("a >> 1 :", a >> 1) # Output: 2  (Binary: 0010)


# numbers = [1, 2, 3, 4, 5]

# print(numbers)
# # Check if 3 is in the list
# print("3 in numbers : ", 3 in numbers)  # Output: True
# print("8 in numbers :", 8 in numbers)  # Output: True

# # Check if 6 is not in the list
# print("4 not in numbers : ", 4 not in numbers)  # Output: True
# print("10 not in numbers : ", 10 not in numbers)  # Output: True

# list1 = [1, 2, 3]
# print("list 1 : ", list1)
# list2 = [1, 2, 3]
# print("list 2 : ", list2)
# list3 = list1
# print("list1 is list2 : ", list1 is list2)      # Output: False (Different memory locations)
# print("list1 == list2 : ", list1 == list2)      # Output: True (Same values but different objects)
# print("list1 is not list2 : ", list1 is not list2) 
# print("list1 is list3 : ", list1 is list3)


# result = 10 + 5 * 2 ** 3 / 4 - 1
# print("10 + 5 * 2 ** 3 / 4 - 1 : ", result)  # Output: 14.0


a = int(input("Enter First Number : "))
b = int(input("Enter Second Number : "))

max_value = a if a > b else b
print("Maximum:", max_value)  # Output: Maximum: 20

# import math  # Import math module

# print("abs(-10) :", abs(-10))                 # Absolute Value
# print("pow(2, 3) :", pow(2, 3))               # Power (2^3)
# print("round(3.6) :", round(3.6))             # Round to nearest integer (Up)
# print("round(3.4) :", round(3.4))             # Round to nearest integer (Down)
# print("min(10, 20, 5, 30) :", min(10, 20, 5, 30))  # Minimum value
# print("max(10, 20, 5, 30) :", max(10, 20, 5, 30))  # Maximum value
# print("math.sqrt(25) :", math.sqrt(25))       # Square root of 25
# print("math.ceil(3.2) :", math.ceil(3.2))     # Ceiling (Rounds up)
# print("math.floor(3.9) :", math.floor(3.9))   # Floor (Rounds down)



"""Assignment  4"""
# # Input from the user
# year = int(input("Enter a year: "))

# # Check leap year condition
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(year, "is a Leap Year")
# else:
#     print(year, "is NOT a Leap Year")

# Input from the user
# n = int(input("Enter a positive integer: "))

# # Initialize sum
# total = 0

# # Loop through numbers from 1 to n
# for i in range(1, n + 1):
#     if i % 3 != 0:  # Exclude numbers divisible by 3
#         total += i

# # Print the result
# print("Sum of first", n, "natural numbers (excluding multiples of 3):", total)



"""Assignnment 5 pattern prinnting
"""
# for i in range(1, 201):  # Loop from 1 to 200
#     if i % 16 == 0:  
#         print("Terminating program at:", i)
#         break  # Stop the loop if the number is divisible by 16
#     if i % 3 == 0 or i % 5 == 0:
#         continue  # Skip numbers that are multiples of 3 or 5
#     print(i)  # Print numbers that are not skipped


# for i in range(1, 6):  # Loop from 1 to 5
#     for j in range(1, i + 1):  # Print numbers from 1 to i
#         print(j, end=" ")  # Print in the same line
#     print()  # Move to the next line after inner loop


# for i in range(1, 6):  # Loop from 1 to 5
#     print(str(i) * i,)  # Print the number 'i', repeated 'i' times


# for i in range(6, 1, -1):  # Loop from 6 down to 1
#     for j in range(i):  # Print numbers from 0 to i-1
#         print(j, end=" ")
    # print()  # Move to the next line

# num = 1  # Start from 1
# for i in range(1, 6):  # Loop for 5 rows
#     print((str(num) + " ") * i)  # Print 'num' repeated 'i' times
#     num += 2  # Increment by 2 to get the next odd number
