# Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Function to find prime numbers in a list
def find_primes(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

# Input from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

# Call the function and print the result
prime_numbers = find_primes(numbers)
print(f"The prime numbers in the list: {prime_numbers}")
