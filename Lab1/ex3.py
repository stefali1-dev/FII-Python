# Exercise 1: Count occurrences of the first string in the second string
def count_occurrences(first_str, second_str):
    count = 0
    start = 0
    while start < len(second_str):
        start = second_str.find(first_str, start)
        if start == -1:
            break
        count += 1
        start += len(first_str)
    return count

# Input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

# Call the function and display the result
occurrences = count_occurrences(str1, str2)
print(f"Number of occurrences of '{str1}' in '{str2}': {occurrences}")
