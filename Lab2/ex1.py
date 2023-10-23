# Function to generate the first n numbers in the Fibonacci sequence
def generate_fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence

# Input from the user
n = int(input("Enter the value of n: "))

# Call the function and print the result
fibonacci_list = generate_fibonacci(n)
print(f"The first {n} numbers in the Fibonacci sequence: {fibonacci_list}")
