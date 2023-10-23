# Exercise 2: Convert UpperCamelCase to lowercase_with_underscores
def camel_to_underscore(input_str):
    result = [input_str[0].lower()]  # Start with the first character in lowercase
    for char in input_str[1:]:
        if char.isupper():
            result.extend(['_', char.lower()])
        else:
            result.append(char)
    return ''.join(result)

# Input from the user
str1 = input("Enter a string in UpperCamelCase: ")

# Call the function and display the result
converted_str = camel_to_underscore(str1)
print(f"Converted string from UpperCamelCase to lowercase_with_underscores: {converted_str}")
