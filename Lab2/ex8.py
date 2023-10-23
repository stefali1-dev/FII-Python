# Function to generate lists of characters based on ASCII code divisibility
def generate_character_lists(x=1, strings=None, flag=True):
    if not strings:
        return []

    result = []
    for string in strings:
        char_list = []
        for char in string:
            ascii_code = ord(char)
            if (flag and ascii_code % x == 0) or (not flag and ascii_code % x != 0):
                char_list.append(char)
        result.append(char_list)
    return result

# Example input
x = 2
string_list = ["test", "hello", "lab002"]
flag = False

# Call the function and print the result
result_lists = generate_character_lists(x, string_list, flag)
print(result_lists)
