
def partition(array, left, right):
	pivot = array[right-1]
	j=left
	for i in range(left, right-1):
		if array[i]<pivot:
			tmp=array[i]
			array[i]=array[j]
			array[j]=tmp
			j+=1
	array[right-1]=array[j]
	array[j]=pivot
	return j

def sort_level(array, left, right):
	if left+1<right:
		i = partition(array, left, right)
		sort_level(array, left, i)
		sort_level(array, i+1, right)

def sort(array):
	"""
	quicksort the array and return the result
	time complexity: O(n*log(n))
	"""
	sort_level(array, 0, len(array))
	return array
	
