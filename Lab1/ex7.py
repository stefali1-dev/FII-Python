import re

# Function to extract the first number from a text
def extract_first_number(text):
    match = re.search(r'\d+', text)
    if match:
        return int(match.group())
    else:
        return None

# Input from the user
text = input("Enter a text: ")

# Call the function and print the result
result = extract_first_number(text)
if result is not None:
    print(f"The first number extracted from the text is: {result}")
else:
    print("No number found in the text.")
