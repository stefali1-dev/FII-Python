# Function to check if a number is a palindrome
def is_palindrome(number):
    return str(number) == str(number)[::-1]

# Function to find palindrome numbers and the greatest palindrome number
def find_palindromes(numbers):
    palindrome_list = [num for num in numbers if is_palindrome(num)]
    greatest_palindrome = max(palindrome_list) if palindrome_list else None
    return len(palindrome_list), greatest_palindrome

# Example input
number_list = [121, 123, 1331, 4554, 12321, 54321]

# Call the function and print the result
palindrome_count, greatest_palindrome = find_palindromes(number_list)
print(f"Number of palindrome numbers: {palindrome_count}")
print(f"The greatest palindrome number: {greatest_palindrome}")
