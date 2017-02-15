from tree_2_3 import Tree23
from tree_2_3 import Node23
from random import shuffle
import unittest

class TreeTest(unittest.TestCase):
	def X_test_one_element(self):
		tree = Tree23()
		tree.insert(6)
		print()
		print(tree.getString())
		assert tree.getList() == [6]
	
	def X_test_two_elements(self):
		tree = Tree23()
		tree.insert(2)
		tree.insert(4)
		print()
		print(tree.getString())
		assert tree.getList() == [2, 4]
	
	def test_many_elements(self):
		tree = Tree23()
		data = list(range(0, 64))
		dataCopy = list(data)
		shuffle(dataCopy)
		for i in dataCopy:
			tree.insert(i)
			print("inserting "+str(i))
			print(tree.getString())
		print()
		print(tree.getString())
		print("expected: "+str(data))
		print("got:      "+str(tree.getList()))
		assert tree.getList() == data
	
	def X_test_constructed_tree(self):
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
