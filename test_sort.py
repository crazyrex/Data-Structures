from tree_sort import sort
import unittest

class SortTest(unittest.TestCase):
	def test_simple_cases(self):
		assert sort([5, 4, 1, 2, 3]) == [1, 2, 3, 4, 5]
		assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
		assert sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
		assert sort([2, 3, 4, 1]) == [1, 2, 3, 4]

if __name__ == '__main__':
    unittest.main()
    
