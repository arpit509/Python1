# def sum_numbers(*args):
#     total = 0
#     for num in args:
#         total += num
#     return total

# # Testing sum_numbers
# print("Sum 1 (1, 2, 3):", sum_numbers(1, 2, 3))             # Output: 6
# print("Sum 2 ( 10, 20):", sum_numbers(10, 20))              # Output: 30
# print("Sum 3 (5):", sum_numbers(5))                   # Output: 5
# print("Sum 4:(0)", sum_numbers())                    # Output: 0

"""----------------------------------------------------------------------------------------------------------"""

# def person_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")
#     print()  # Just for spacing

# # Testing person_info
# person_info(name="Alice", age=25, city="Delhi")
# person_info(name="Bob", profession="Engineer")
# person_info(name = "Arpit", profession = "Student")

"""----------------------------------------------------------------------------------------------------------"""

def display_details(*args, **kwargs):
    print("Positional arguments (args):")
    for item in args:
        print(item)

    print("Keyword arguments (kwargs):")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print()  # Just for spacing

# Testing display_details
display_details(1, 2, 3, name="Arpit", age=19)
display_details("apple", "banana", color="red", size="medium")
