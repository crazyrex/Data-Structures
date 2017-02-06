#!python

import string


def is_palindrome(text):
	"""A string of characters is a palindrome if it reads the same forwards and
	backwards, ignoring punctuation, whitespace, and letter casing"""
	# implement is_palindrome_iterative and is_palindrome_recursive below, then
	# change this to call your implementation to verify it passes all tests
	assert isinstance(text, str)
	#return is_palindrome_iterative(text)
	return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
	left=0
	right=len(text)-1
	while left<right:
		lc=ord(text[left])
		if lc>=ord('A') and lc<=ord('Z'):
			lc
	
	for i in range(0, len(text)//2):
		if text[i]!=text[-i-1]:
			return False
	return True

def is_palindrome_recursive(text, i=0):
	if i>=len(text)//2: return True
	elif text[i]!=text[-i-1]: return False
	else: return is_palindrome_recursive(text, i+1)

def main():
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) > 0:
		for arg in args:
			is_pal = is_palindrome(arg)
			result = 'PASS' if is_pal else 'FAIL'
			str_not = 'a' if is_pal else 'not a'
			print('{}: {} is {} palindrome'.format(result, repr(arg), str_not))
	else:
		print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
		print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
	main()
