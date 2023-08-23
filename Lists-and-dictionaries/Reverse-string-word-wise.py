# Reverse the given string word wise. That is, the last word in given string should come at 1st place, last second word at 
# 2nd place and so on. Individual words should remain as it is.


string = input()
 
# spliting words in the given string
# using slicing reverse the words
s = string.split()[::-1]
 
# joining the reversed string and
# printing the output
print(" ".join(s))
