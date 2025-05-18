# To install the requests library, run this command in your terminal or command prompt:
# pip install requests

import requests

# Take URL input from the user
url = input("Enter a URL: ")

try:
    # Fetch the HTML content using requests.get()
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        content = response.text  # Get the response content as text
        print("First 500 characters of the response:\n")
        print(content[:500])     # Print only the first 500 characters
    else:
        print(f"Failed to fetch the URL. Status code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")
