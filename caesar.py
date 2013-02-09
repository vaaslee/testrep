#This function will take the character and the key
#s = character; k = key;
def tocrypte(s,k):
	#alphabet = list of English letters
	if s == " ":
		return " "
	if s == ",":
		return ","
	if s == ".":
		return "."
	if s == "!":
		return "!"
	if s == "?":
		return "?"
	if s == "-":
		return "-"
	if s == ":":
		return ":"
	if s == ";":
		return ";"
	alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]
	#ind = index of character
	ind = alphabet.index(s) + k
	#letter = returning letter
	if ind > 25:
		ind = ind - 25 -1
	letter = alphabet[ind]
	return letter
#
#
#

#word = our word
word = raw_input("Type the word you want to encrypt(enter /exit to close the program):")
if word != "/exit":
	key = input("Type the key:")
i = 0
while word != "/exit":
	result = []
	for x in word:
		result.append(tocrypte(word[i], key))
		i = i + 1
	result = ''.join(result)
	print result
	word = raw_input("Type the word you want to encrypt(enter /exit to close the program):")
	if word != "/exit":
		i = 0
		key = input("Type the key:")

		 

