def word_lengths(sentence):
    return {word: len(word) for word in sentence.split()}

# Input the sentence from the user
sentence = input("Enter a sentence: ")

# Call the function and print the result
result = word_lengths(sentence)
print(result)