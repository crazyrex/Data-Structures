#!python

def stringSearch(pattern, text):
	if len(pattern) == 0:
		return True
	i = 0
	while (i < len(text)-len(pattern)):
		j = 0
		while text[j+i] == pattern[j]:
			j += 1
			if j == len(pattern):
				return True
		i += 1
	return False
