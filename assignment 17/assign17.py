from numpy import square
import math_utils

radius = float(input("Enter the radius of the circle: "))
print("Area of circle(radius = 5): ", math_utils.area_of_circle(radius))

factorial = int(input("Enter a number to find its factorial: "))
print("Factorial of 5: ", math_utils.factorial_of_number(factorial))

square = int(input("Enter a number to find if it is a perfect square: "))   
print("Is 16 a perfect square? ", math_utils.is_perfect_square(square))


print(dir(math_utils))
