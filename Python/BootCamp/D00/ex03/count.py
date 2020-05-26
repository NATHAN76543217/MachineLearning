import string

def text_analyzer(*text):
	"""
	This function counts the number of upper characters, lower characters, punctuation and spaces in a given text.
	"""
	if len(text) > 1:
		print("ERROR")
		return
	if len(text) == 0 or isinstance(text[0], str) == 0:
		text = []
		text.append(input("What is the text to analyse?\n>> "))	ponctu_list = string.punctuation
	nb_upper = 0
	nb_lower = 0
	nb_ponct = 0
	nb_spaces = 0
	letters = 0
	for char in text[0]:
		letters += 1
		if char == ' ':
			nb_spaces += 1
		elif char.isupper():
			nb_upper += 1
		elif char.islower():
			nb_lower += 1
		elif char in ponctu_list:
			nb_ponct += 1
	print("The text contains %s characters:" %letters, '\n')
	print("-", nb_upper, "upper letters\n")
	print("-", nb_lower, "lower letters\n")
	print("-", nb_ponct, "punctuation marks\n")
	print("-", nb_spaces, "spaces")