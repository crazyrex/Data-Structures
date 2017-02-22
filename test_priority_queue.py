from heap_priority_queue import PriorityQueue
import unittest

class PriorityQueueTest(unittest.TestCase):
	
	def test_in_order(self):
		queue = PriorityQueue()
		
		queue.enqueue(0, 'a')
		queue.enqueue(1, 'b')
		queue.enqueue(2, 'c')
		
		assert queue.dequeue() == 'a'
		assert queue.dequeue() == 'b'
		assert queue.dequeue() == 'c'
		
	def test_backwords(self):
		queue = PriorityQueue()
		
		queue.enqueue(2, 'c')
		queue.enqueue(1, 'b')
		queue.enqueue(0, 'a')
		
		assert queue.dequeue() == 'a'
		assert queue.dequeue() == 'b'
		assert queue.dequeue() == 'c'
	
	def test_out_of_order(self):
		queue = PriorityQueue()
		
		queue.enqueue(2, 'c')
		queue.enqueue(3, 'd')
		queue.enqueue(0, 'a')
		queue.enqueue(1, 'b')
		
		assert queue.dequeue() == 'a'
		assert queue.dequeue() == 'b'
		assert queue.dequeue() == 'c'
		assert queue.dequeue() == 'd'

if __name__ == '__main__':
    unittest.main()

