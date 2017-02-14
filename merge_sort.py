
def merge(array0, array1):
	i0 = 0
	i1 = 0
	out = []
	
	while (True):
		if i0<len(array0) and i1<len(array1):
			if (array0[i0]<array1[i1]):
				out.append(array0[i0])
				i0+=1
			else:
				out.append(array1[i1])
				i1+=1
		elif i0<len(array0):
			out.append(array0[i0])
			i0+=1
		elif i1<len(array1):
			out.append(array1[i1])
			i1+=1
		else:
			break
	
	return out

def sort_level(array, left, right):
	if (left+1>=right):
		return [array[left]]
	else:
		middle=int((right-left)/2)+left
		array0=sort_level(array, left, middle)
		array1=sort_level(array, middle, right)
		return merge(array0, array1)

def sort(array):
	"""
	merge sort the array and return the result
	time complexity: O(n*log(n))
	"""
	return sort_level(array, 0, len(array))
	
