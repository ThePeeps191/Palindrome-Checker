# Make The Function
def palindrome_checker():
	word = input("Enter Your Word:\n")
	return word == word[len(word)::-1]

print(palindrome_checker())
# Try Typing "nope". It Will Print "False" To The Screen

print(palindrome_checker())
# Try Typing "racecar". It Will Print "True" To The Screen
