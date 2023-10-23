import math

# Function to calculate the GCD of a list of numbers
def find_gcd(numbers):
    if len(numbers) < 2:
        return None  # GCD is not defined for fewer than two numbers
    gcd_result = numbers[0]
    for i in range(1, len(numbers)):
        gcd_result = math.gcd(gcd_result, numbers[i])
    return gcd_result

# Read numbers from the console and store them in a list
try:
    input_numbers = input("Enter numbers separated by spaces: ").split()
    numbers = [int(num) for num in input_numbers]
    gcd = find_gcd(numbers)
    if gcd:
        print(f"The greatest common divisor (GCD) of the numbers is: {gcd}")
    else:
        print("Please enter at least two numbers.")
except ValueError:
    print("Invalid input. Please enter valid numbers separated by spaces.")
