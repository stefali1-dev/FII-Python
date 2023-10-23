# Function to count the number of 1 bits in the binary representation of a number
def count_ones_bits(number):
    binary_str = bin(number)[2:]  # Convert to binary and remove the '0b' prefix
    count = binary_str.count('1')
    return count

# Input from the user
num = input("Enter a number: ")

try:
    num = int(num)
    ones_count = count_ones_bits(num)
    print(f"Number of 1 bits in the binary representation of {num}: {ones_count}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
