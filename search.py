#!python

def linear_search(array, item):
	"""return the first index of item in array or None if item is not found"""
	# implement linear_search_iterative and linear_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	# return linear_search_iterative(array, item)
	return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
	# loop over all array values until item is found
	for index, value in enumerate(array):
		if item == value:
			return index  # found
	return None  # not found


def linear_search_recursive(array, item, index=0):
	if index>=len(array):
		return None
	elif array[index]==item:
		return index
	else:
		return linear_search_recursive(array, item, index+1)
	# once implemented, change linear_search to call linear_search_recursive
	# to verify that your recursive implementation passes all tests below


def binary_search(array, item):
	"""return the index of item in sorted array or None if item is not found"""
	# implement binary_search_iterative and binary_search_recursive below, then
	# change this to call your implementation to verify it passes all tests
	return binary_search_iterative(array, item)
	# return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
	left=0
	right=len(array)
	
	while (left+1<right):
		center=(left+right)/2
		if array[center]>item:
			right=center
		else:
			left=center
	
	if array[left]==item:
	  	return left
	else:
		return None
	# once implemented, change binary_search to call binary_search_iterative
	# to verify that your iterative implementation passes all tests below


def binary_search_recursive(array, item, left=None, right=None):
	
	if not left: left=0
	if not right: right=len(array)
	center=(left+right)/2
	if array[center]>item:
		right=center
	else:
		left=center
	
	if left+1==right:
		if array[left]==item:
		  	return left
		else:
			return None
	else:
		return binary_search_recursive(array, item, left, right)
	# once implemented, change binary_search to call binary_search_recursive
	# to verify that your recursive implementation passes all tests below
