# Function to find items that appear exactly x times in multiple lists
def find_items_appearing_x_times(x, *lists):
    item_count = {}
    for lst in lists:
        for item in lst:
            if item in item_count:
                item_count[item] += 1
            else:
                item_count[item] = 1
    result = [item for item, count in item_count.items() if count == x]
    return result

# Example input
list1 = [1, 2, 3, 2, 4]
list2 = [2, 3, 5, 6, 5]
list3 = [1, 3, 5, 7, 7]
x = 2

# Call the function and print the result
result_list = find_items_appearing_x_times(x, list1, list2, list3)
print(result_list)
