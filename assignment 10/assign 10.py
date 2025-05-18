                                # # Creating a dictionary with countries and their capitals
# countries = {
#     "India": "New Delhi",
#     "USA": "Washington, D.C.",
#     "France": "Paris",
#     "Japan": "Tokyo",
#     "Germany": "Berlin"
# }

# # Printing all keys (country names)
# print("Country Names:", countries.keys())

# # Printing all values (capital cities)
# print("Capital Cities:", countries.values())

# # Printing all key-value pairs
# print("Pairs:", countries.items())

# # Accessing the capital of a given country using get()
# country_name = input("Enter a country name to get its capital: ")
# capital = countries.get(country_name, "Country not found")
# print("Capital of", country_name, ":", capital)


"""Assignment 5 and 6 """

# Creating a dictionary with countries and their capitals
countries = {
    "India": "New Delhi",
    "China": "Beijing",
    "Japan": "Tokyo",
    
}

# 1. Create a copy of the dictionary and clear the original one
countries_copy = countries.copy()  # Copy the dictionary
countries.clear()  # Clear the original dictionary

print("Copied Dictionary:", countries_copy)
print("Original Dictionary after clearing:", countries)

# 2. Merge two dictionaries (Asian and European countries)
asia_countries = {
    "India": "New Delhi",
    "China": "Beijing",
    
}

print("Asian Countries:", asia_countries)

europe_countries = {
    "Germany": "Berlin",
    "France": "Paris",
}
print("European Countries:", europe_countries)

# Merge dictionaries
  # Start with a copy of the first dictionary
asia_countries.update(europe_countries)  # Merge the second dictionary

print("Merged Dictionary:", asia_countries)
