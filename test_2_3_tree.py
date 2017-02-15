from tree_2_3 import Tree23
from tree_2_3 import Node23
import unittest

class TreeTest(unittest.TestCase):
	def test_one_element(self):
		tree = Tree23()
		tree.insert(6)
		print()
		print(tree.getString())
		assert tree.getList() == [6]
	
	def test_two_elements(self):
		tree = Tree23()
		tree.insert(2)
		tree.insert(4)
		print()
		print(tree.getString())
		assert tree.getList() == [2, 4]
	
	def test_many_elements(self):
		tree = Tree23()
		tree.insert(2)
		tree.insert(4)
		tree.insert(7)
		tree.insert(5)
		tree.insert(8)
		print()
		print(tree.getString())
		assert tree.getList() == [2, 4]
	
	def test_constructed_tree(self):
		tree = Tree23()
		tree.root = Node23(
			Node23(
				None,
				11,
				None),
			12,
			Node23(
				None,
				13,
				None)
		)
		print()
		print(tree.getString())
		assert tree.getList() == [2, 6, 9]

if __name__ == '__main__':
    unittest.main()
