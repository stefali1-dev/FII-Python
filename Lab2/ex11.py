# Function to sort a list of string tuples based on the 3rd character of the 2nd element
def sort_tuples_based_on_3rd_character(tuples):
    return sorted(tuples, key=lambda tup: tup[1][2])

# Example input
tuples = [('abc', 'bcd'), ('abc', 'zza')]

# Call the function and print the result
sorted_tuples = sort_tuples_based_on_3rd_character(tuples)
print(sorted_tuples)
