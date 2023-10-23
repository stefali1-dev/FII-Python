# Function to create a list of tuples from multiple lists
def create_tuples_from_lists(*lists):
    max_length = max(len(lst) for lst in lists)
    result = []

    for i in range(max_length):
        tuple_items = tuple(lst[i] if i < len(lst) else None for lst in lists)
        result.append(tuple_items)

    return result

# Example input
list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

# Call the function and print the result
result_tuples = create_tuples_from_lists(list1, list2, list3)
print(result_tuples)
