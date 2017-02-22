from heap import MinHeap

class PriorityQueue:
	
	def __init__(self):
		self.heap = MinHeap()
	
	def enqueue(self, priority, item):
		self.heap.push((priority, item))
	
	def dequeue(self):
		try:
			self.heap.pop()[1]
		except:
			return None

