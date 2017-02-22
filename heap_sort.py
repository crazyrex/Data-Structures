from heap import MinHeap

def sort(array):
	heap = MinHeap()
	for i in array:
		heap.push(i)
	
	out=[]
	while True:
		try:
			out.append(heap.pop())
		except:
			break;
	
	return out

