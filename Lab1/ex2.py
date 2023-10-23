# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "AEIOUaeiou"
    vowel_count = 0
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

# Read a string from the console
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the string is: {vowel_count}")
