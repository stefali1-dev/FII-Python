# Function to count the number of words in a text
def count_words(text):
    words = text.split()
    return len(words)

# Input from the user
text = input("Enter a text: ")

# Call the function and print the result
word_count = count_words(text)
print(f"Number of words in the text: {word_count}")
