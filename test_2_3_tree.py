from tree_2_3 import Tree23
import unittest

class TreeTest(unittest.TestCase):
	def test_one_element(self):
		tree = Tree23()
		tree.insert(6)
		assert tree.getList() == [6]
	
	def test_two_elements(self):
		tree = Tree23()
		tree.insert(2)
		tree.insert(4)
		assert tree.getList() == [2, 4]

if __name__ == '__main__':
    unittest.main()
