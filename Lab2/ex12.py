# Function to group words by rhyme (ending with the same 2 letters)
def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else:
            rhymes[rhyme] = [word]

    grouped_words = list(rhymes.values())
    return grouped_words

# Example input
word_list = ['ana', 'banana', 'carte', 'arme', 'parte']

# Call the function and print the result
grouped_by_rhyme = group_by_rhyme(word_list)
print(grouped_by_rhyme)
