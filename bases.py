#!python

import string

def digitToVal(digitStr):
	digit=ord(digitStr)
	if digit>=ord('0') and digit<=ord('9'):
		return digit-ord('0')
	elif digit>=ord('a') and digit<=ord('z'):
		return digit-ord('a')+10
	elif digit>=ord('A') and digit<=ord('Z'):
		return digit-ord('A')+10
	else:
		return 0

def valToDigit(val):
	if val>=0 and val<=9:
		return chr(val+ord('0'))
	elif val>=10 and val<=36:
		return chr(val-10+ord('a'))
	else:
		return 0

def decode(str_num, base):
	"""
	Decode given number from given base to base 10.
	str_num -- string representation of number in given base
	base -- base of given number
	"""
	assert 2 <= base <= 36
	
	out=0
	for i in str_num:
		out=out*base+digitToVal(i)
	
	return out

def encode(num, base):
	"""
	Encode given number from base 10 to given base.
	num -- the number in base 10
	base -- base to convert to
	"""
	assert 2 <= base <= 36
	
	out=""
	
	while (num!=0):
		out=valToDigit(num%base)+out
		num/=base
	
	return out
	

def convert(str_num, base1, base2):
	"""
	Convert given number from base1 to base2.
	"""
	assert 2 <= base1 <= 36
	assert 2 <= base2 <= 36
	return encode(decode(str_num, base1), base2)


def main():
	import sys
	args = sys.argv[1:]  # Ignore script file name
	if len(args) == 3:
		str_num = args[0]
		base1 = int(args[1])
		base2 = int(args[2])
		result = convert(str_num, base1, base2)
		print('{} in base {} is {} in base {}'.format(str_num, base1, result, base2))
	else:
		print('Usage: {} number base1 base2'.format(sys.argv[0]))


if __name__ == '__main__':
	main()
