"""----------------------------------------------------------------------------------------------------------------------"""
# def calculate_area(length, width):
#     area = length * width
#     return area

# length1 = int(input("Enter the length of the rectangle: "))
# width1 = int(input("Enter the width of the rectangle: "))
# print("Area of the rectangle =  ", calculate_area(length1, width1))




"""-----------------------------------------------------------------------------------------------"""

# def greet_user(name, greeting = "Hello"):

#     return f"{greeting}, {name}!"

# print(greet_user("Arpit"))
# print(greet_user("Rishab", "Greetings"))
# print(greet_user("Prem", "Good Morning"))

"""-----------------------------------------------------------------------------------------------------"""

def math_operations(a,b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b
    return add, sub, mul, div

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
add, sub, mul, div = math_operations(a,b)
print("Addition: ", add)
print("Subtraction: ", sub)
print("Multiplication: ", mul)
print("Divide : ", div)