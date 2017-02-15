from tree_2_3 import Tree23

def sort(array):
	tree = Tree23()
	for i in array:
		tree.insert(i)
	return tree.getList()
	
