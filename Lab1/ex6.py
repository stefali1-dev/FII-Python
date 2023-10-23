# Function to validate if a number is a palindrome
def is_palindrome(number):
    number_str = str(number)
    return number_str == number_str[::-1]

# Input from the user
num = input("Enter a number: ")

try:
    num = int(num)
    if is_palindrome(num):
        print(f"{num} is a palindrome.")
    else:
        print(f"{num} is not a palindrome.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
