# Aadil has been provided with a sentence in the form of a string as a function parameter. The task is to implement a function so as to print the sentence such that each word in the sentence is reversed. A word is a combination of characters without any spaces.
# Example:
# Input Sentence: "Hello, I am Aadil!"
# The expected output will print, ",olleH I ma !lidaA".

def reverse_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1]for word in words]
    reversed_sentence = ' '.join(reversed_words)
    print(reversed_sentence)


input_sentence = input()
reverse_word(input_sentence)
