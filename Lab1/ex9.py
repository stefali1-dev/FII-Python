# Function to determine the most common letter in a string
def most_common_letter(input_string):
    # Convert the string to lowercase to treat 'A' and 'a' as the same character
    input_string = input_string.lower()
    letter_count = {}

    # Count the occurrences of letters
    for char in input_string:
        if char.isalpha():
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    if letter_count:
        most_common = max(letter_count, key=letter_count.get)
        return most_common, letter_count[most_common]
    else:
        return None, 0

# Input from the user
text = input("Enter a string: ")

# Call the function and print the result
common_letter, count = most_common_letter(text)
if common_letter is not None:
    print(f"The most common letter is '{common_letter}' ({count} times).")
else:
    print("No letters found in the input.")
