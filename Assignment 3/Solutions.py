"""
#Solutions_5240100507_2025.py
# 1 Reverse the string "Programming"
text = "Programming"
print("Reversed string:", text[::-1])

#2 Get initials in uppercase
initials = ".".join([word[0]. upper() for word in full_name".split()]) +"."
print("Initials:", initials)

#3 Palindrome checker
word = input("Enter a word")
if word == word [::-1]:
    print("It's a palindrome")
else: 
    print("It's not a palindrome")

#4 Word count in a sentence
sentence = input("Enter sentence:")
print ("Word count:", len(sentence.split()))


#5 Replace "is" with "was" 
text = "This is a string and it is an example."
print("Modified string:", text.replace("is", "was"))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""



"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""



"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
"""