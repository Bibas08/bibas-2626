# Indexing and Slicing
   #Given the string s = "PythonPractice", what are the outputs of:
   
s = "PythonPractice"
print(s[1])
print(s[-3:])
print(s[2:7])
# Output: 'y'

#Reverse a String
   #Write a one-liner to reverse the string "developer" using slicing.
s = "developer"
reversed_s = s[::-1]
print(reversed_s)  

# Count Vowels
# Write a function that counts the number of vowels in a given string.
vowels = "aeiouAEIOU"
def count_vowels(s):
 return sum(1 for char in s.lower() if char in "aeiou")

#Check for Palindrome
  # Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.
  
def is_palindrome(s):
   cleaned = ''.join(c.lower() for c in s if c.isalnum())
   return cleaned == cleaned[::-1]


text = "   hello world! welcome to Python.   "
cleaned = text.strip().title().replace("Python", "Programming")

def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)



