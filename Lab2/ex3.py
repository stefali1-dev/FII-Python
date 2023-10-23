# Function to perform set operations on two lists a and b
def set_operations(a, b):
    intersection = list(set(a).intersection(b))
    union = list(set(a).union(b))
    difference_a_b = list(set(a).difference(b))
    difference_b_a = list(set(b).difference(a))
    return intersection, union, difference_a_b, difference_b_a

# Input from the user
list_a = input("Enter the elements of list a separated by spaces: ").split()
list_b = input("Enter the elements of list b separated by spaces: ").split()

list_a = [int(item) for item in list_a]
list_b = [int(item) for item in list_b]

# Call the function and print the result
intersection, union, diff_a_b, diff_b_a = set_operations(list_a, list_b)
print(f"Intersection of a and b: {intersection}")
print(f"Union of a and b: {union}")
print(f"a - b: {diff_a_b}")
print(f"b - a: {diff_b_a}")
