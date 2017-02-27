from heap import MinHeap

class PriorityQueueItem:
	def __init__(self, priority, value):
		self.priority = priority
		self.value = value
	
	def __lt__(self, other):
		return self.priority < other.priority
	
	def __gt__(self, other):
		return self.priority > other.priority
	
	def __le__(self, other):
		return self.priority <= other.priority
	
	def __ge__(self, other):
		return self.priority >= other.priority
	
	def __ne__(self, other):
		return self.priority != other.priority
	
	def __eq__(self, other):
		return self.priority == other.priority

class PriorityQueue:
	
	def __init__(self):
		self.heap = MinHeap()
	
	def enqueue(self, priority, item):
		self.heap.push(PriorityQueueItem(priority, item))
	
	def dequeue(self):
		try:
			return self.heap.pop().value
		except:
			return None

